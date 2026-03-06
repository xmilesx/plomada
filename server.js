/**
 * server.js — Express server for Plomada Lead Engine.
 *
 * Serves the static frontend from public/ and exposes two API endpoints:
 *   POST /api/leads  — create a new lead
 *   GET  /api/leads  — list all leads
 */

const express = require('express');
const path = require('path');
const { initDatabase, insertLead, getAllLeads } = require('./database');

const app = express();
const PORT = process.env.PORT || 3000;

// --- Middleware ---

// Parse JSON request bodies (for API calls from the frontend)
app.use(express.json());

// Serve static files (HTML, CSS, JS) from the public/ directory
app.use(express.static(path.join(__dirname, 'public')));

// --- API Routes ---

/**
 * POST /api/leads
 * Receives lead data from the intake form and saves it to SQLite.
 * Returns the new lead's id.
 */
app.post('/api/leads', (req, res) => {
  try {
    const lead = req.body;

    // Basic validation: at least one meaningful field should be present
    if (!lead.lead_source && !lead.project_type && !lead.neighborhood) {
      return res.status(400).json({
        error: 'Please fill in at least the lead source, project type, or neighborhood.',
      });
    }

    const id = insertLead(lead);
    res.status(201).json({ id, message: 'Lead saved successfully.' });
  } catch (err) {
    console.error('Error saving lead:', err);
    res.status(500).json({ error: 'Failed to save lead.' });
  }
});

/**
 * GET /api/leads
 * Returns all leads as a JSON array, newest first.
 */
app.get('/api/leads', (req, res) => {
  try {
    const leads = getAllLeads();
    res.json(leads);
  } catch (err) {
    console.error('Error fetching leads:', err);
    res.status(500).json({ error: 'Failed to fetch leads.' });
  }
});

// --- Start the server ---

async function start() {
  // Initialize the database (creates tables if needed) before accepting requests
  await initDatabase();

  app.listen(PORT, () => {
    console.log(`Plomada Lead Engine running at http://localhost:${PORT}`);
  });
}

start();
