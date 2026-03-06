/**
 * leads.js — Fetches all leads from the API and renders them as a table.
 */

const container = document.getElementById('leads-container');

/**
 * Human-readable labels for the stored enum values.
 * Keeps the display clean without changing what's in the database.
 */
const LABELS = {
  // Lead Source
  referral: 'Referral',
  google: 'Google',
  instagram: 'Instagram',
  houzz: 'Houzz',
  architect: 'Architect',
  repeat_client: 'Repeat Client',

  // Project Type
  gut_renovation: 'Gut Reno',
  kitchen: 'Kitchen',
  bathroom: 'Bathroom',
  addition: 'Addition',
  basement: 'Basement',
  whole_house: 'Whole House',
  adu: 'ADU',

  // Neighborhood
  capitol_hill: 'Capitol Hill',
  georgetown: 'Georgetown',
  dupont_circle: 'Dupont Circle',
  logan_circle: 'Logan Circle',
  shaw: 'Shaw',
  petworth: 'Petworth',
  brookland: 'Brookland',
  columbia_heights: 'Columbia Hts',
  cleveland_park: 'Cleveland Park',
  takoma: 'Takoma',
  anacostia: 'Anacostia',
  navy_yard: 'Navy Yard',
  adams_morgan: 'Adams Morgan',
  woodley_park: 'Woodley Park',

  // Budget
  under_50k: '<$50k',
  '50k_100k': '$50–100k',
  '100k_200k': '$100–200k',
  '200k_400k': '$200–400k',
  '400k_750k': '$400–750k',
  '750k_plus': '$750k+',
  not_discussed: 'Not Discussed',

  // Generic
  other: 'Other',
};

/**
 * Look up a human-readable label, falling back to the raw value.
 */
function label(value) {
  if (!value) return '—';
  return LABELS[value] || value;
}

/**
 * Return the CSS class for a verdict badge.
 */
function verdictBadgeClass(verdict) {
  if (!verdict) return 'badge badge-pending';
  const v = verdict.toLowerCase();
  if (v === 'go') return 'badge badge-go';
  if (v === 'no-go' || v === 'nogo') return 'badge badge-nogo';
  if (v === 'maybe') return 'badge badge-maybe';
  return 'badge badge-pending';
}

/**
 * Format a datetime string into a short readable form.
 */
function formatDate(dateStr) {
  if (!dateStr) return '—';
  const d = new Date(dateStr);
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
}

/**
 * Fetch leads from the API and render the table (or an empty state).
 */
async function loadLeads() {
  try {
    const response = await fetch('/api/leads');
    const leads = await response.json();

    if (leads.length === 0) {
      container.innerHTML = `
        <div class="empty-state">
          <p>No leads yet.</p>
          <a href="/" class="btn btn-primary">Add Your First Lead</a>
        </div>
      `;
      return;
    }

    // Build the table HTML
    let html = `
      <div class="leads-table-wrap">
        <table class="leads-table">
          <thead>
            <tr>
              <th>#</th>
              <th>Date</th>
              <th>Source</th>
              <th>Type</th>
              <th>Neighborhood</th>
              <th>Budget</th>
              <th>Score</th>
              <th>Verdict</th>
            </tr>
          </thead>
          <tbody>
    `;

    for (const lead of leads) {
      const score = lead.qualification_score != null ? lead.qualification_score : '—';
      const verdict = lead.verdict || 'Pending';
      const badgeClass = verdictBadgeClass(lead.verdict);

      html += `
        <tr>
          <td>${lead.id}</td>
          <td>${formatDate(lead.created_at)}</td>
          <td>${label(lead.lead_source)}</td>
          <td>${label(lead.project_type)}</td>
          <td>${label(lead.neighborhood)}</td>
          <td>${label(lead.stated_budget)}</td>
          <td>${score}</td>
          <td><span class="${badgeClass}">${verdict}</span></td>
        </tr>
      `;
    }

    html += `
          </tbody>
        </table>
      </div>
    `;

    container.innerHTML = html;
  } catch (err) {
    console.error('Failed to load leads:', err);
    container.innerHTML = `
      <div class="empty-state">
        <p>Failed to load leads. Is the server running?</p>
      </div>
    `;
  }
}

// Load leads when the page opens
loadLeads();
