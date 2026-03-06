/**
 * intake.js — Handles the lead intake form submission.
 *
 * Collects all form field values, POSTs them as JSON to /api/leads,
 * and shows a success or error message.
 */

const form = document.getElementById('lead-form');
const flash = document.getElementById('flash');
const submitBtn = document.getElementById('submit-btn');

/**
 * Show a flash message (success or error) at the top of the form.
 */
function showFlash(message, type) {
  flash.textContent = message;
  flash.className = `flash flash-${type}`;
  flash.style.display = 'block';

  // Auto-hide after 5 seconds
  setTimeout(() => {
    flash.style.display = 'none';
  }, 5000);
}

/**
 * Collect all form field values into a plain object.
 * Field names match the database columns.
 */
function collectFormData() {
  return {
    lead_source: document.getElementById('lead_source').value,
    project_type: document.getElementById('project_type').value,
    neighborhood: document.getElementById('neighborhood').value,
    stated_budget: document.getElementById('stated_budget').value,
    timeline: document.getElementById('timeline').value,
    property_status: document.getElementById('property_status').value,
    architect_involved: document.getElementById('architect_involved').value,
    decision_maker: document.getElementById('decision_maker').value,
    funding_type: document.getElementById('funding_type').value,
    notes: document.getElementById('notes').value,
  };
}

/**
 * Handle form submission: send data to the API, show result.
 */
form.addEventListener('submit', async (e) => {
  e.preventDefault();

  // Disable the button to prevent double-submission
  submitBtn.disabled = true;
  submitBtn.textContent = 'Saving...';

  try {
    const data = collectFormData();

    const response = await fetch('/api/leads', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });

    const result = await response.json();

    if (response.ok) {
      showFlash(`Lead #${result.id} saved. `, 'success');
      form.reset(); // Clear the form for the next entry
    } else {
      showFlash(result.error || 'Something went wrong.', 'error');
    }
  } catch (err) {
    console.error('Submit error:', err);
    showFlash('Network error — is the server running?', 'error');
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = 'Save Lead';
  }
});
