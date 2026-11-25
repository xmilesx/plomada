#!/usr/bin/env python3
"""
DC Property Feasibility Report Generator
Generates clean, minimal PDF reports from property data using HTML/CSS templates.

Dependencies:
    pip install jinja2 weasyprint --break-system-packages

Usage:
    from generate_report import generate_feasibility_report
    generate_feasibility_report(property_data, output_path)
"""

import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS

# Template directory (same as this script)
TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_feasibility_report(data: dict, output_path: str) -> str:
    """
    Generate a PDF feasibility report from property data.
    
    Args:
        data: Dictionary containing all property data fields
        output_path: Path for output PDF file
    
    Returns:
        Path to generated PDF
    """
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template('report_template.html')
    
    # Add defaults for missing fields
    defaults = {
        'date': datetime.now().strftime('%B %d, %Y'),
        'constraints': '',
        'historic_district': None,
        'hprb_required': 'No',
        'permits': [],
        'violations': None,
        'mor_options': [],
        'bza_triggers': [],
        'high_risks': [],
        'medium_risks': [],
        'next_steps': [],
        'sources': [],
    }
    
    # Merge defaults with provided data
    report_data = {**defaults, **data}
    
    # Render HTML
    html_content = template.render(**report_data)
    
    # Generate PDF
    html = HTML(string=html_content, base_url=TEMPLATE_DIR)
    html.write_pdf(output_path)
    
    return output_path


def format_currency(value: int | float) -> str:
    """Format number as currency."""
    return f"${value:,.0f}"


def format_sf(value: int | float) -> str:
    """Format number as square feet."""
    return f"{value:,.0f} SF"


# Example usage with sample data
if __name__ == '__main__':
    sample_data = {
        # Header
        'address': '100 Example Place NW (fictional sample)',
        'date': 'February 2, 2026',
        
        # Key Metrics
        'zone': 'RF-1',
        'lot_sf': '1,463',
        'max_buildable_sf': '2,262',
        'max_units': '2',
        
        # Site Photos - Visual Review Observations (Oct 2018 Google Street View)
        'street_view_img': None,
        'satellite_img': None,
        'aerial_notes': '''STREET VIEW (Oct 2018): 2-story tan/buff brick rowhouse with cellar. Flat roof with decorative brick parapet/cornice (not true mansard - typical 1920s DC construction). Front porch with masonry stairs, red/orange painted iron railings. Mature deciduous trees partially obscure facade. Attached rowhouse - party walls both sides.

SATELLITE (Aug 2023): Flat membrane roof visible on entire row. Rear yards vary in depth - 100 appears mid-block. Alley runs E-W behind row (~15\' wide, paved). No visible rooftop HVAC units or solar panels on 100. Neighbor at 102 has chimney visible on shared party wall - extends above roofline.

NEIGHBOR OBSERVATIONS: 98 Example appears similar 2-story, no visible 3rd floor addition. 102 Example has chimney on party wall with 100 - key constraint for vertical addition. No obvious pop-backs visible from satellite on immediate neighbors. Alley access appears adequate for construction staging.''',
        
        # Constraints
        'constraints': 'Adjacent chimney at 102 Example extends above roofline on shared party wall - requires neighbor agreement to cap, extend, or work around for any 3rd story addition. 10\' rear wall extension rule (Subtitle E § 205.4) limits horizontal expansion without survey of 98/102 rear walls. Lot width (~16.5\') does not support additional off-street parking without BZA relief.',
        
        # Property Identification
        'ssl': '0000-0000 (Square 0000, Lot 0000)',
        'owner': '[Owner name from PropertyQuest]',
        'owner_address': '[Requires OTR detail page - login to mytax.dc.gov]',
        'assessment': '$000,000 (sample)',
        'last_sale': '[Date · price, verify via Recorder of Deeds]',
        'year_built': '1926',
        
        # Zoning - Detailed
        'zone_description': 'Residential Flat - moderate-density rowhouse zone',
        'max_height': '35\' / 3 stories MOR · 40\' with BZA SE (Subtitle E § 303.1, 303.3)',
        'max_lot_occupancy': '60% (878 SF) MOR · 70% with BZA SE (Subtitle E § 304.1, 5201.1)',
        'front_setback': 'Equal to setback of adjacent bldgs or avg of block face (Subtitle E § 307)',
        'rear_yard': '20\' minimum (Subtitle E § 306.1)',
        'side_yard': 'None required for attached rowhouse (Subtitle E § 305.1)',
        'pervious': 'None required - lot < 1,800 SF (Subtitle E § 308.1)',
        'lot_area_per_unit': '900 SF per unit = max 2 units on 1,463 SF lot (Subtitle U § 320.2)',
        'parking_required': '0.5 spaces/unit in RF-1 = 1 space for 2 units (Subtitle C § 701.5) - may be waived via special exception if no alley access or site constraints',
        
        # Historic
        'historic_district': None,
        'hprb_required': 'No - verify via DC SHPO database',
        
        # Existing Conditions
        'living_sf': '1,436',
        'basement_sf': '558',
        'total_building_sf': '1,994',
        'current_stories': '2 + cellar',
        'bed_bath': '4 bed / 1.5 bath (per assessment records)',
        'current_coverage': '~49% (~717 SF)',
        'available_coverage': '~11% (~161 SF) to 60% MOR',
        
        # Permits - Requires Scout DC login
        'permits': [],
        'violations': '[Requires Scout DC login - create free Access DC account at access.dc.gov then search scout.dcra.dc.gov]',
        
        # Development Potential
        'current_height': '~22-25\' (2 stories typical for 1926 construction)',
        'vertical_potential': '+1 story to 35\' MOR, or +2 stories to 40\' with BZA SE. CONSTRAINT: 102\'s chimney on party wall blocks standard 3rd floor without neighbor agreement.',
        'vertical_sf': '700-800 SF per floor (estimate based on ~49% coverage)',
        'current_rear_depth': '[Survey required - estimate 30-40\' from satellite]',
        'ten_foot_rule': 'Yes - Subtitle E § 205.4. Extension limited to 10\' beyond furthest rear wall of adjacent buildings.',
        'horizontal_potential': 'Pop-back within 10\' rule + 60% lot coverage. VERIFY: measure 98 & 102 rear walls.',
        'horizontal_sf': 'Up to ~161 SF (to 60% coverage) or per 10\' rule calculation',
        'underpin_potential': 'Likely feasible - 1926 cellar typically ~6.5\' ceiling, can achieve 8\'+ with underpinning. Requires structural engineer assessment.',
        'max_above_grade': '~2,262 SF (3 floors × ~754 SF @ 60% coverage)',
        'max_below_grade': '~878 SF (full footprint @ 60% coverage)',
        'max_total': '~3,140 SF (ESTIMATE ONLY - verify with architect)',
        
        # Regulatory
        'recommended_path': 'Matter-of-right path for 2-unit conversion with interior renovation. Any 3rd story requires either (a) neighbor agreement for 102\'s chimney, or (b) design that works around chimney. Full pop-back requires survey of 98/102 rear walls for 10\' rule calculation.',
        'mor_options': [
            'Interior renovation (residential permit: 4-8 weeks)',
            '2-unit conversion with new C of O (6-10 weeks)',
            'Pop-back ≤10\' beyond both 98 & 102 rear walls (4-8 weeks + survey)',
            '3rd story to 35\' if chimney cleared/designed around (6-10 weeks)',
        ],
        'bza_triggers': [
            'Height > 35\' up to 40\' (Subtitle E § 303.3)',
            'Rear extension > 10\' beyond adjacent bldgs (Subtitle E § 205.5)',
            'Lot occupancy > 60% up to 70% (Subtitle E § 5201.1(a))',
            'Parking waiver if no alley access/site constraints (Subtitle C § 703)',
        ],
        'mor_timeline': '4-10 weeks (plan review + permit issuance)',
        'bza_timeline': '4-6 months from complete filing',
        
        # ANC/SMD
        'anc': 'ANC 4C (verify via anc.dc.gov)',
        'anc_commissioner': '[Look up SMD 4C0X commissioner at anc.dc.gov]',
        'walk_score': None,
        
        # Recent BZA Cases
        'recent_bza_cases': [
            {'number': '[Search DCOZ]', 'relief': 'Search izis.dc.gov for Example Pl NW cases', 'result': 'TBD', 'result_class': 'warning'},
        ],
        
        # Comparable Sales
        'comparable_sales': None,
        
        # Risks - Enhanced
        'high_risks': [
            'CHIMNEY AT 102 EXAMPLE PL: Visible on party wall, extends above roofline. ANY vertical addition requires neighbor agreement to cap, extend, or redesign roof to work around. Without agreement, 3rd story not feasible.',
            '10\' REAR WALL RULE: Pop-back limited by 98 & 102 rear walls. Must survey both to determine allowable extension. Exceeding 10\' requires BZA special exception.',
            'PERMIT/VIOLATION HISTORY: Unknown - Scout DC search required. Open violations or unpermitted work could delay closing or require remediation.',
        ],
        'medium_risks': [
            'Party wall condition - 1926 brick, may require structural assessment for vertical load',
            'Cornice/parapet - decorative brick parapet should be preserved or replicated per zoning (Subtitle E § 206)',
            'Foundation capacity for underpinning - requires structural engineer assessment before bidding',
            'Lot width (~16.5\') insufficient for off-street parking without creative solution or waiver',
            'Heritage trees in front yard - if protected, may constrain future front improvements',
        ],
        
        # Next Steps
        'next_steps': [
            'Search Scout DC for permit/violation history (requires free Access DC login)',
            'Pull OTR detail page for owner mailing address and assessment breakdown',
            'Survey 98 & 102 rear walls for 10\' rule calculation (or order survey)',
            'Contact owner of 102 re: chimney agreement (get in writing before closing)',
            'Order title search for liens, easements, party wall agreements',
            'Check DCOZ IZIS database for recent BZA cases on Example Pl',
            'Engage architect for preliminary design within MOR envelope',
            'Request DDOT public space permit timeline if any work in ROW planned',
            'Confirm DC Water capacity for 2-unit conversion (typically adequate)',
        ],
        
        # Zoning Citations
        'zoning_citations': [
            {'section': 'Subtitle E § 201', 'description': 'RF Zone - General Provisions', 'url': 'https://online.encodeplus.com/regs/washington-dc/doc-viewer.aspx#secid-818'},
            {'section': 'Subtitle E § 303.1', 'description': 'Height MOR (35\' / 3 stories)', 'url': 'https://online.encodeplus.com/regs/washington-dc/doc-viewer.aspx#secid-830'},
            {'section': 'Subtitle E § 303.3', 'description': 'Height SE (40\')', 'url': 'https://online.encodeplus.com/regs/washington-dc/doc-viewer.aspx#secid-830'},
            {'section': 'Subtitle E § 304.1', 'description': 'Lot Occupancy MOR (60%)', 'url': 'https://online.encodeplus.com/regs/washington-dc/doc-viewer.aspx#secid-831'},
            {'section': 'Subtitle E § 205.4', 'description': '10\' Rear Extension Rule', 'url': 'https://online.encodeplus.com/regs/washington-dc/doc-viewer.aspx#secid-822'},
            {'section': 'Subtitle E § 205.5', 'description': 'Rear Extension SE', 'url': 'https://online.encodeplus.com/regs/washington-dc/doc-viewer.aspx#secid-822'},
            {'section': 'Subtitle E § 206', 'description': 'Rooftop Elements / Cornice', 'url': 'https://online.encodeplus.com/regs/washington-dc/doc-viewer.aspx#secid-823'},
            {'section': 'Subtitle E § 306.1', 'description': 'Rear Yard (20\' min)', 'url': 'https://online.encodeplus.com/regs/washington-dc/doc-viewer.aspx#secid-833'},
            {'section': 'Subtitle E § 307', 'description': 'Front Setback', 'url': 'https://online.encodeplus.com/regs/washington-dc/doc-viewer.aspx#secid-834'},
            {'section': 'Subtitle E § 5201.1', 'description': 'SE Standards (lot occupancy, height)', 'url': 'https://online.encodeplus.com/regs/washington-dc/doc-viewer.aspx#secid-883'},
            {'section': 'Subtitle U § 320.2', 'description': 'Conversion - 900 SF/unit', 'url': 'https://online.encodeplus.com/regs/washington-dc/doc-viewer.aspx#secid-1574'},
            {'section': 'Subtitle C § 701.5', 'description': 'Parking (0.5/unit RF-1)', 'url': 'https://online.encodeplus.com/regs/washington-dc/doc-viewer.aspx#secid-670'},
            {'section': 'Subtitle C § 703', 'description': 'Parking Waiver SE', 'url': 'https://online.encodeplus.com/regs/washington-dc/doc-viewer.aspx#secid-672'},
        ],
        
        # Sources
        'sources': [
            {'name': 'DC OTR Real Property Database', 'url': 'https://mytax.dc.gov'},
            {'name': 'Scout DC (Permits/Violations)', 'url': 'https://scout.dcra.dc.gov'},
            {'name': 'DC ZR16 (Zoning Regulations)', 'url': 'https://online.encodeplus.com/regs/washington-dc'},
            {'name': 'DC Atlas Pro (Mapping)', 'url': 'https://opendata.dc.gov/apps/dc-atlas-pro'},
            {'name': 'DCOZ IZIS (BZA Cases)', 'url': 'https://izis.dc.gov'},
            {'name': 'Google Street View', 'url': 'https://maps.google.com'},
            {'name': 'Google Earth', 'url': 'https://earth.google.com'},
        ],
    }
    
    output = '/mnt/user-data/outputs/sample_feasibility.pdf'
    generate_feasibility_report(sample_data, output)
    print(f"Report generated: {output}")
