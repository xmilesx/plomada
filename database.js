/**
 * database.js — SQLite setup, schema creation, and query helpers for Plomada leads.
 *
 * Uses sql.js (pure JS SQLite compiled to WASM) so no native build tools are needed.
 * The database file is persisted to disk at ./data/plomada.db.
 */

const initSqlJs = require('sql.js');
const fs = require('fs');
const path = require('path');

// Where the SQLite file lives on disk
const DATA_DIR = path.join(__dirname, 'data');
const DB_PATH = path.join(DATA_DIR, 'plomada.db');

// Module-level reference to the database instance
let db = null;

/**
 * Initialize the database: load from disk (or create fresh), then ensure
 * the leads table exists. Returns the db instance.
 */
async function initDatabase() {
  const SQL = await initSqlJs();

  // Create the data directory if it doesn't exist
  if (!fs.existsSync(DATA_DIR)) {
    fs.mkdirSync(DATA_DIR, { recursive: true });
  }

  // Load existing database file or start fresh
  if (fs.existsSync(DB_PATH)) {
    const fileBuffer = fs.readFileSync(DB_PATH);
    db = new SQL.Database(fileBuffer);
  } else {
    db = new SQL.Database();
  }

  // Create the leads table if it doesn't already exist.
  // Each field maps to a column the intake form collects.
  db.run(`
    CREATE TABLE IF NOT EXISTS leads (
      id              INTEGER PRIMARY KEY AUTOINCREMENT,
      lead_source     TEXT,          -- How did they find us? (referral, google, etc.)
      project_type    TEXT,          -- What kind of project? (gut reno, addition, etc.)
      neighborhood    TEXT,          -- DC neighborhood (Capitol Hill, Georgetown, etc.)
      stated_budget   TEXT,          -- What budget did they mention?
      timeline        TEXT,          -- When do they want to start/finish?
      property_status TEXT,          -- Own it, under contract, etc.
      architect_involved TEXT,       -- Yes / No / Not yet
      decision_maker  TEXT,          -- Are we talking to the decision maker?
      funding_type    TEXT,          -- Cash, construction loan, HELOC, etc.
      notes           TEXT,          -- Free-form notes
      created_at      TEXT DEFAULT (datetime('now', 'localtime')),
      qualification_score INTEGER,  -- Numeric score (filled later by AI or manual)
      verdict         TEXT,          -- Go / No-Go / Maybe (filled later)
      draft_response  TEXT           -- Suggested reply to the lead (filled later)
    )
  `);

  // Persist the freshly-created schema to disk
  saveDatabase();

  return db;
}

/**
 * Write the current in-memory database to disk.
 * Call this after every write operation.
 */
function saveDatabase() {
  if (!db) return;
  const data = db.export();
  const buffer = Buffer.from(data);
  fs.writeFileSync(DB_PATH, buffer);
}

/**
 * Insert a new lead into the database.
 * @param {Object} lead — object with keys matching the column names
 * @returns {number} the id of the newly inserted row
 */
function insertLead(lead) {
  // Use db.run for INSERT — it doesn't need a prepared statement cursor
  db.run(`
    INSERT INTO leads (
      lead_source, project_type, neighborhood, stated_budget,
      timeline, property_status, architect_involved, decision_maker,
      funding_type, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `, [
    lead.lead_source || null,
    lead.project_type || null,
    lead.neighborhood || null,
    lead.stated_budget || null,
    lead.timeline || null,
    lead.property_status || null,
    lead.architect_involved || null,
    lead.decision_maker || null,
    lead.funding_type || null,
    lead.notes || null,
  ]);

  saveDatabase();

  // sql.js quirk: last_insert_rowid() via exec can return 0.
  // Use a direct SELECT on max(id) instead — safe because we just inserted.
  const result = db.exec('SELECT max(id) as id FROM leads');
  return result[0].values[0][0];
}

/**
 * Get all leads, newest first.
 * Returns an array of plain objects.
 */
function getAllLeads() {
  const result = db.exec(`
    SELECT * FROM leads ORDER BY created_at DESC
  `);

  // db.exec returns [{ columns: [...], values: [[...], ...] }]
  // Convert to an array of objects for easier consumption
  if (result.length === 0) return [];

  const columns = result[0].columns;
  return result[0].values.map(row => {
    const obj = {};
    columns.forEach((col, i) => {
      obj[col] = row[i];
    });
    return obj;
  });
}

/**
 * Get a single lead by id. Returns the lead object or null.
 */
function getLeadById(id) {
  const stmt = db.prepare('SELECT * FROM leads WHERE id = ?');
  stmt.bind([id]);

  let lead = null;
  if (stmt.step()) {
    const row = stmt.getAsObject();
    lead = row;
  }

  stmt.free();
  return lead;
}

module.exports = {
  initDatabase,
  insertLead,
  getAllLeads,
  getLeadById,
};
