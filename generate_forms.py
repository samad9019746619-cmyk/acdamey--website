"""
Generates all 11 exam application form HTML files.
Run once: python generate_forms.py
"""

import os

FORMS_DIR = os.path.join(os.path.dirname(__file__), "forms")
os.makedirs(FORMS_DIR, exist_ok=True)

CONTACTS = """
  <div class="top-bar">
    <span>📞 <a href="tel:8019546619">8019546619</a> &nbsp;|&nbsp; <a href="tel:9849822213">9849822213</a></span>
    <span>Opp. Jannat Studio, Shah Ali Banda, Hyderabad 500002</span>
  </div>"""

HEADER = """
  <header>
    <div class="brand">
      <img src="../images/logo.jpeg" alt="Academy Logo">
      <div class="brand-text">
        <h1>The Neo Global Educational Academy</h1>
        <span>Hyderabad, Telangana</span>
      </div>
    </div>
    <a href="index.html" class="btn-back">← All Forms</a>
  </header>"""

CSS = """
    :root{--emerald-dark:#022c22;--emerald-deep:#064e3b;--emerald-main:#047857;--emerald-light:#10b981;--emerald-soft:#ecfdf5;--gold-dark:#b48c1e;--gold-main:#d4af37;--gold-light:#fde047;--bg-cream:#faf9f6;--border:#e2e8f0;--text-main:#0f172a;--text-muted:#64748b}
    *{box-sizing:border-box;margin:0;padding:0}
    html{scroll-behavior:smooth}
    body{font-family:'Inter',sans-serif;background:var(--bg-cream);color:var(--text-main);min-height:100vh;display:flex;flex-direction:column;-webkit-font-smoothing:antialiased}
    h1,h2,h3,h4{font-family:'Playfair Display',serif;color:var(--emerald-dark)}
    a{text-decoration:none;color:inherit;transition:.2s}

    .top-bar{background:var(--emerald-dark);color:#e2e8f0;font-size:.82rem;padding:8px 24px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px}
    .top-bar a{color:#fde047;font-weight:700}
    header{background:rgba(255,255,255,.95);backdrop-filter:blur(16px);border-bottom:1px solid var(--border);padding:14px 24px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:100;box-shadow:0 2px 12px rgba(2,44,34,.07)}
    .brand{display:flex;align-items:center;gap:14px}
    .brand img{width:48px;height:48px;border-radius:50%;border:2px solid var(--gold-main)}
    .brand-text h1{font-size:1.1rem;font-family:'Playfair Display',serif;color:var(--emerald-dark)}
    .brand-text span{font-size:.68rem;color:var(--emerald-main);font-weight:700;text-transform:uppercase;letter-spacing:1px}
    .btn-back{display:inline-flex;align-items:center;gap:6px;padding:8px 16px;background:var(--emerald-dark);color:#fff;border-radius:50px;font-size:.84rem;font-weight:700}
    .btn-back:hover{background:var(--gold-main);color:var(--emerald-dark)}

    main{flex:1;max-width:800px;width:100%;margin:40px auto 60px;padding:0 20px}
    .form-header{margin-bottom:30px}
    .form-header .pill{display:inline-block;background:rgba(212,175,55,.12);border:1px solid var(--gold-main);color:var(--gold-main);padding:4px 16px;border-radius:50px;font-size:.76rem;font-weight:800;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:10px}
    .form-header h2{font-size:clamp(1.6rem,3vw,2.2rem);margin-bottom:8px}
    .form-header p{color:var(--text-muted);font-size:.95rem}

    .form-card{background:#fff;border-radius:16px;padding:32px;box-shadow:0 4px 20px rgba(2,44,34,.08);border:1px solid var(--border)}
    .form-section{background:#f8fafc;border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:22px}
    .form-section-title{display:flex;align-items:center;gap:10px;font-size:1rem;font-weight:800;color:var(--emerald-deep);margin-bottom:16px;padding-bottom:10px;border-bottom:1px solid var(--border)}
    .form-section-num{background:var(--emerald-dark);color:var(--gold-light);width:26px;height:26px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:.82rem;font-weight:800;flex-shrink:0}
    .form-row{display:grid;grid-template-columns:1fr 1fr;gap:16px}
    .input-group{margin-bottom:14px}
    .input-group label{display:block;font-size:.78rem;font-weight:700;color:var(--emerald-dark);margin-bottom:5px;text-transform:uppercase;letter-spacing:.4px}
    .input-group input,.input-group select,.input-group textarea{width:100%;padding:11px 14px;border:1.5px solid var(--border);border-radius:9px;font-family:inherit;font-size:.93rem;transition:.25s;background:#fff;color:var(--text-main)}
    .input-group input:focus,.input-group select:focus,.input-group textarea:focus{border-color:var(--gold-main);outline:none;box-shadow:0 0 0 3px rgba(212,175,55,.15)}
    .input-group input[type=file]{padding:9px 12px;cursor:pointer}
    .required-mark{color:#dc2626}
    .field-hint{font-size:.75rem;color:var(--text-muted);margin-top:4px}
    .error-msg{font-size:.76rem;color:#dc2626;margin-top:4px;display:none;font-weight:600}
    .input-group.has-error input,.input-group.has-error select,.input-group.has-error textarea{border-color:#dc2626}

    .consent-wrap{background:#fffbeb;border:1px solid #fde68a;padding:14px;border-radius:10px;font-size:.84rem;color:#92400e;margin-bottom:20px;display:flex;gap:10px;align-items:flex-start}
    .consent-wrap input{margin-top:3px;flex-shrink:0;width:16px;height:16px;cursor:pointer;accent-color:var(--emerald-dark)}

    .btn-submit{width:100%;padding:15px;background:var(--gold-main);color:var(--emerald-dark);border:none;border-radius:50px;font-size:1.05rem;font-weight:800;cursor:pointer;transition:all .25s;display:flex;align-items:center;justify-content:center;gap:10px}
    .btn-submit:hover:not(:disabled){background:var(--gold-light);transform:translateY(-2px);box-shadow:0 8px 24px rgba(212,175,55,.4)}
    .btn-submit:disabled{opacity:.6;cursor:not-allowed;transform:none}
    .spinner{display:none;width:18px;height:18px;border:3px solid rgba(2,44,34,.2);border-top-color:var(--emerald-dark);border-radius:50%;animation:spin .7s linear infinite}
    @keyframes spin{to{transform:rotate(360deg)}}

    /* Success screen */
    .success-screen{display:none;text-align:center;padding:40px 20px}
    .success-icon{width:72px;height:72px;background:#dcfce7;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 18px;color:var(--emerald-main)}
    .success-icon svg{width:36px;height:36px}
    .ref-badge{display:inline-block;background:var(--emerald-soft);border:2.5px dashed var(--emerald-main);padding:10px 24px;border-radius:12px;font-size:1.3rem;font-weight:800;color:var(--emerald-dark);margin:14px 0;letter-spacing:1px}
    .wa-btns{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:22px}
    .btn-wa{padding:12px;border-radius:10px;font-weight:700;font-size:.9rem;text-align:center;display:block;transition:.2s}
    .btn-wa1{background:#25d366;color:#fff}
    .btn-wa2{background:#128c7e;color:#fff}
    .btn-wa:hover{opacity:.88}

    .api-error{background:#fef2f2;border:1px solid #fecaca;color:#dc2626;padding:12px 16px;border-radius:9px;font-size:.88rem;margin-bottom:16px;display:none}

    footer{background:#011d17;color:#94a3b8;text-align:center;padding:22px;font-size:.82rem;border-top:1px solid rgba(212,175,55,.2);margin-top:auto}
    footer strong{color:var(--gold-main)}
    footer a{color:#94a3b8;margin:0 8px}
    footer a:hover{color:var(--gold-light)}

    @media(max-width:640px){
      .form-row{grid-template-columns:1fr}
      .wa-btns{grid-template-columns:1fr}
      .form-card{padding:20px}
    }
    @media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}"""

SHARED_JS = """
  const API_BASE = '';

  function validate(form) {
    let ok = true;
    form.querySelectorAll('[required]').forEach(el => {
      const grp = el.closest('.input-group');
      const err = grp?.querySelector('.error-msg');
      const val = el.value.trim();
      if (!val) {
        if(grp) grp.classList.add('has-error');
        if(err){ err.textContent = 'This field is required.'; err.style.display='block'; }
        ok = false;
      } else {
        if(grp) grp.classList.remove('has-error');
        if(err) err.style.display='none';
      }
      // Indian phone validation
      if (el.id === 'f_phone' && val && !/^[6-9]\\d{9}$/.test(val)) {
        if(grp) grp.classList.add('has-error');
        if(err){ err.textContent = 'Enter a valid 10-digit Indian mobile number.'; err.style.display='block'; }
        ok = false;
      }
    });
    return ok;
  }

  function buildWhatsApp(ref, examName, name, phone) {
    const msg = encodeURIComponent(
      '*New Enquiry: ' + examName + '*\\n' +
      'Ref: ' + ref + '\\n' +
      'Name: ' + name + '\\n' +
      'Phone: ' + phone
    );
    document.getElementById('btnWa1').href = 'https://wa.me/918019546619?text=' + msg;
    document.getElementById('btnWa2').href = 'https://wa.me/919849822213?text=' + msg;
  }

  async function submitForm(event, courseId, courseName, category) {
    event.preventDefault();
    const form = event.target;
    if (!validate(form)) return;

    const btn = document.getElementById('btnSubmit');
    const spinner = document.getElementById('btnSpinner');
    const apiErr = document.getElementById('apiError');
    btn.disabled = true;
    if(spinner) spinner.style.display = 'inline-block';
    apiErr.style.display = 'none';

    const resumeInput = document.getElementById('f_resume');
    let resumeNote = '';
    if (resumeInput && resumeInput.files[0]) {
      resumeNote = resumeInput.files[0].name;
    }

    const payload = {
      course_id: courseId,
      course_name: courseName,
      program_category: category,
      full_name: (document.getElementById('f_name')?.value || '').trim(),
      dob: document.getElementById('f_dob')?.value || '2000-01-01',
      gender: document.getElementById('f_gender')?.value || 'Not specified',
      student_mobile: (document.getElementById('f_phone')?.value || '').trim(),
      email: (document.getElementById('f_email')?.value || '').trim() || null,
      address: ((document.getElementById('f_address')?.value || '') + ', ' +
                (document.getElementById('f_city')?.value || '') + ', ' +
                (document.getElementById('f_state')?.value || '')).trim().replace(/^,\\s*|,\\s*$/g,''),
      city: (document.getElementById('f_city')?.value || 'Hyderabad').trim(),
      state: (document.getElementById('f_state')?.value || 'Telangana').trim(),
      pincode: (document.getElementById('f_pincode')?.value || '500000').trim() || '500000',
      last_qualification: (document.getElementById('f_education')?.value || '').trim(),
      prev_institution: (document.getElementById('f_institution')?.value || '').trim() || null,
      course_specific_data: (document.getElementById('f_specific')?.value || resumeNote || '').trim() || null,
      consent_given: true,
      application_date: new Date().toLocaleString('en-IN')
    };

    try {
      const res = await fetch(API_BASE + '/api/applications/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Submission failed. Please try again.');

      document.getElementById('formSection').style.display = 'none';
      const ss = document.getElementById('successScreen');
      ss.style.display = 'block';
      document.getElementById('refNo').textContent = data.reference_no;
      buildWhatsApp(data.reference_no, courseName, payload.full_name, payload.student_mobile);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch(e) {
      apiErr.textContent = e.message;
      apiErr.style.display = 'block';
      btn.disabled = false;
      if(spinner) spinner.style.display = 'none';
    }
  }"""

FOOTER_HTML = """
<footer>
  <p>&copy; <script>document.write(new Date().getFullYear())</script> The Neo Global Educational Academy, Hyderabad &mdash; Developed by <strong>Mohammed Abdul Samad</strong></p>
  <p style="margin-top:8px">
    <a href="../index.html">Home</a>
    <a href="index.html">All Forms</a>
    <a href="tel:8019546619">📞 8019546619</a>
    <a href="tel:9849822213">📞 9849822213</a>
    <a href="https://wa.me/918019546619" target="_blank">WhatsApp</a>
  </p>
</footer>"""

def success_block():
    return """
      <div class="success-screen" id="successScreen">
        <div class="success-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>
        <h2 style="color:var(--emerald-dark);font-size:1.7rem;margin-bottom:8px">Application Submitted!</h2>
        <p style="color:var(--text-muted);margin-bottom:5px">Your application has been received. Your reference number:</p>
        <div class="ref-badge" id="refNo">TNGA-XXXX</div>
        <p style="font-size:.88rem;color:var(--text-muted);margin-top:12px">Save this reference number. Contact us on WhatsApp for next steps.</p>
        <div class="wa-btns">
          <a href="#" id="btnWa1" class="btn-wa btn-wa1" target="_blank">WhatsApp 8019546619</a>
          <a href="#" id="btnWa2" class="btn-wa btn-wa2" target="_blank">WhatsApp 9849822213</a>
        </div>
        <button class="btn-submit" onclick="location.reload()" style="margin-top:20px;max-width:260px;margin-left:auto;margin-right:auto">Submit Another</button>
      </div>"""

def common_fields():
    return """
            <div class="input-group">
              <label>Full Name <span class="required-mark">*</span></label>
              <input type="text" id="f_name" placeholder="Enter your full name" required autocomplete="name">
              <div class="error-msg"></div>
            </div>
            <div class="form-row">
              <div class="input-group">
                <label>Mobile Number <span class="required-mark">*</span></label>
                <input type="tel" id="f_phone" placeholder="10-digit mobile number" required maxlength="10" autocomplete="tel">
                <div class="error-msg"></div>
              </div>
              <div class="input-group">
                <label>Email Address</label>
                <input type="email" id="f_email" placeholder="Optional" autocomplete="email">
              </div>
            </div>
            <div class="input-group">
              <label>Residential Address <span class="required-mark">*</span></label>
              <textarea id="f_address" rows="2" placeholder="House no, street, area..." required></textarea>
              <div class="error-msg"></div>
            </div>
            <div class="form-row">
              <div class="input-group">
                <label>City <span class="required-mark">*</span></label>
                <input type="text" id="f_city" placeholder="e.g. Hyderabad" required autocomplete="address-level2">
                <div class="error-msg"></div>
              </div>
              <div class="input-group">
                <label>State <span class="required-mark">*</span></label>
                <select id="f_state" required>
                  <option value="">Select state</option>
                  <option value="Telangana" selected>Telangana</option>
                  <option value="Andhra Pradesh">Andhra Pradesh</option>
                  <option value="Karnataka">Karnataka</option>
                  <option value="Maharashtra">Maharashtra</option>
                  <option value="Tamil Nadu">Tamil Nadu</option>
                  <option value="Kerala">Kerala</option>
                  <option value="Gujarat">Gujarat</option>
                  <option value="Rajasthan">Rajasthan</option>
                  <option value="Uttar Pradesh">Uttar Pradesh</option>
                  <option value="Delhi">Delhi</option>
                  <option value="Other">Other</option>
                </select>
                <div class="error-msg"></div>
              </div>
            </div>
            <div class="input-group">
              <label>Highest Education / Qualification <span class="required-mark">*</span></label>
              <input type="text" id="f_education" placeholder="e.g. 10th Pass / 12th Pass / Graduate" required>
              <div class="error-msg"></div>
            </div>"""

def resume_field():
    return """
            <div class="input-group">
              <label>Resume / CV Upload</label>
              <input type="file" id="f_resume" accept=".pdf,.doc,.docx">
              <div class="field-hint">Optional. PDF or Word document, max 5 MB. The file name will be noted in your application.</div>
            </div>"""

def build_form(filename, title, pill, exam_name, course_id, category, specific_field_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title} | The Neo Global Educational Academy</title>
  <meta name="description" content="Apply for {exam_name} coaching at The Neo Global Educational Academy, Hyderabad."/>
  <link rel="icon" type="image/jpeg" href="../images/logo.jpeg"/>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap" rel="stylesheet">
  <style>{CSS}
  </style>
</head>
<body>
{CONTACTS}
{HEADER}

<main>
  <div class="form-header">
    <div class="pill">{pill}</div>
    <h2>Application Form</h2>
    <p>Fill in the details below to apply for <strong>{exam_name}</strong> coaching at The Neo Global Educational Academy, Hyderabad.</p>
  </div>

  <div class="form-card">
    <div id="apiError" class="api-error"></div>

    <div id="formSection">
      <form id="appForm" onsubmit="submitForm(event,'{course_id}','{exam_name}','{category}')" novalidate>
        <input type="hidden" value="{course_id}">

        <div class="form-section">
          <div class="form-section-title"><span class="form-section-num">1</span> Personal Information</div>
{common_fields()}
        </div>

        <div class="form-section">
          <div class="form-section-title"><span class="form-section-num">2</span> Exam Details</div>
{specific_field_html}
{resume_field()}
        </div>

        <div class="consent-wrap">
          <input type="checkbox" id="f_consent" required>
          <label for="f_consent">I confirm the information provided is accurate and consent to its use for admission / coaching enquiry processing by The Neo Global Educational Academy.</label>
        </div>

        <button type="submit" class="btn-submit" id="btnSubmit">
          <span class="spinner" id="btnSpinner"></span>
          Submit Application
        </button>
      </form>
    </div>

{success_block()}
  </div>
</main>

{FOOTER_HTML}

<script>
{SHARED_JS}
</script>
</body>
</html>"""


FORMS = [
    {
        "filename": "neet.html",
        "title": "NEET-UG Application",
        "pill": "Medical Entrance",
        "exam_name": "NEET-UG Medical Coaching",
        "course_id": "neet-prep",
        "category": "neet_jee",
        "specific": """
            <div class="form-row">
              <div class="input-group">
                <label>Target Year <span class="required-mark">*</span></label>
                <select id="f_specific" required>
                  <option value="">Select year</option>
                  <option>2025</option><option>2026</option><option>2027</option>
                </select>
                <div class="error-msg"></div>
              </div>
              <div class="input-group">
                <label>NEET Attempt</label>
                <select id="f_institution">
                  <option value="First attempt">First attempt</option>
                  <option value="Second attempt">Second attempt</option>
                  <option value="Dropper / Repeater">Dropper / Repeater</option>
                </select>
              </div>
            </div>
            <div class="input-group">
              <label>Stream</label>
              <select id="f_gender">
                <option value="BiPC (Bio, Physics, Chemistry)">BiPC (Bio, Physics, Chemistry)</option>
                <option value="PCB">PCB</option>
              </select>
            </div>"""
    },
    {
        "filename": "jee.html",
        "title": "JEE Application",
        "pill": "Engineering Entrance",
        "exam_name": "JEE Main & Advanced Coaching",
        "course_id": "iit-jee-prep",
        "category": "neet_jee",
        "specific": """
            <div class="form-row">
              <div class="input-group">
                <label>Target Year <span class="required-mark">*</span></label>
                <select id="f_specific" required>
                  <option value="">Select year</option>
                  <option>2025</option><option>2026</option><option>2027</option>
                </select>
                <div class="error-msg"></div>
              </div>
              <div class="input-group">
                <label>Target Paper</label>
                <select id="f_institution">
                  <option value="JEE Main only">JEE Main only</option>
                  <option value="JEE Main + Advanced (IIT)">JEE Main + Advanced (IIT)</option>
                  <option value="JEE Main + EAMCET">JEE Main + EAMCET</option>
                </select>
              </div>
            </div>
            <div class="input-group">
              <label>Attempt</label>
              <select id="f_gender">
                <option value="First attempt">First attempt</option>
                <option value="Dropper / Repeater">Dropper / Repeater</option>
              </select>
            </div>"""
    },
    {
        "filename": "cuet.html",
        "title": "CUET Application",
        "pill": "Central University Entrance",
        "exam_name": "CUET (UG) Coaching",
        "course_id": "cuet-ug",
        "category": "degree",
        "specific": """
            <div class="input-group">
              <label>Target Universities <span class="required-mark">*</span></label>
              <input type="text" id="f_specific" placeholder="e.g. JMI, AMU, DU, BHU" required>
              <div class="error-msg"></div>
            </div>
            <div class="input-group">
              <label>Preferred Subjects</label>
              <input type="text" id="f_institution" placeholder="e.g. Commerce, Humanities, Science">
            </div>
            <div class="input-group">
              <label>Gender</label>
              <select id="f_gender">
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="Prefer not to say">Prefer not to say</option>
              </select>
            </div>"""
    },
    {
        "filename": "toss-ssc.html",
        "title": "TOSS SSC Application",
        "pill": "TOSS – Class 10",
        "exam_name": "TOSS SSC (Class 10) Coaching",
        "course_id": "ssc-regular",
        "category": "ssc",
        "specific": """
            <div class="form-row">
              <div class="input-group">
                <label>Exam Year <span class="required-mark">*</span></label>
                <select id="f_specific" required>
                  <option value="">Select</option>
                  <option>2025</option><option>2026</option>
                </select>
                <div class="error-msg"></div>
              </div>
              <div class="input-group">
                <label>Board</label>
                <select id="f_institution">
                  <option value="TOSS (Telangana Open School)">TOSS (Telangana Open School)</option>
                  <option value="AP Open School">AP Open School</option>
                  <option value="NIOS">NIOS</option>
                </select>
              </div>
            </div>
            <div class="input-group">
              <label>Gender</label>
              <select id="f_gender">
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>"""
    },
    {
        "filename": "toss-intermediate.html",
        "title": "TOSS Intermediate Application",
        "pill": "TOSS – Class 12",
        "exam_name": "TOSS Intermediate (Class 12) Coaching",
        "course_id": "inter-mpc",
        "category": "intermediate",
        "specific": """
            <div class="form-row">
              <div class="input-group">
                <label>Group <span class="required-mark">*</span></label>
                <select id="f_specific" required>
                  <option value="">Select group</option>
                  <option value="MPC (Maths, Physics, Chemistry)">MPC (Maths, Physics, Chemistry)</option>
                  <option value="BiPC (Biology, Physics, Chemistry)">BiPC (Biology, Physics, Chemistry)</option>
                  <option value="CEC (Commerce, Economics)">CEC (Commerce, Economics)</option>
                  <option value="HEC (Humanities, Economics)">HEC (Humanities, Economics)</option>
                </select>
                <div class="error-msg"></div>
              </div>
              <div class="input-group">
                <label>Exam Year</label>
                <select id="f_institution">
                  <option>2025</option><option>2026</option>
                </select>
              </div>
            </div>
            <div class="input-group">
              <label>Gender</label>
              <select id="f_gender">
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>"""
    },
    {
        "filename": "upsc.html",
        "title": "UPSC Civil Services Application",
        "pill": "Civil Services",
        "exam_name": "UPSC Civil Services Coaching",
        "course_id": "upsc-ias",
        "category": "pg",
        "specific": """
            <div class="form-row">
              <div class="input-group">
                <label>Optional Subject <span class="required-mark">*</span></label>
                <input type="text" id="f_specific" placeholder="e.g. History, Geography, Public Administration" required>
                <div class="error-msg"></div>
              </div>
              <div class="input-group">
                <label>Attempt Number</label>
                <select id="f_institution">
                  <option value="1st attempt">1st attempt</option>
                  <option value="2nd attempt">2nd attempt</option>
                  <option value="3rd attempt">3rd attempt</option>
                  <option value="4th attempt or more">4th attempt or more</option>
                </select>
              </div>
            </div>
            <div class="input-group">
              <label>Gender</label>
              <select id="f_gender">
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="Prefer not to say">Prefer not to say</option>
              </select>
            </div>"""
    },
    {
        "filename": "ssc-cgl.html",
        "title": "SSC CGL / CHSL Application",
        "pill": "SSC Exams",
        "exam_name": "SSC CGL / CHSL Coaching",
        "course_id": "ssc-cgl",
        "category": "ssc",
        "specific": """
            <div class="form-row">
              <div class="input-group">
                <label>Exam Targeted <span class="required-mark">*</span></label>
                <select id="f_specific" required>
                  <option value="">Select</option>
                  <option value="SSC CGL (Combined Graduate Level)">SSC CGL (Combined Graduate Level)</option>
                  <option value="SSC CHSL (Combined Higher Secondary)">SSC CHSL (Combined Higher Secondary)</option>
                  <option value="SSC MTS">SSC MTS</option>
                  <option value="SSC CPO">SSC CPO</option>
                  <option value="SSC JE">SSC JE</option>
                </select>
                <div class="error-msg"></div>
              </div>
              <div class="input-group">
                <label>Post Preference</label>
                <input type="text" id="f_institution" placeholder="e.g. Inspector, Clerk, Auditor">
              </div>
            </div>
            <div class="input-group">
              <label>Gender</label>
              <select id="f_gender">
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>"""
    },
    {
        "filename": "banking.html",
        "title": "Banking Exams Application",
        "pill": "Banking & Finance",
        "exam_name": "Banking Competitive Exam Coaching",
        "course_id": "banking-ibps",
        "category": "degree",
        "specific": """
            <div class="form-row">
              <div class="input-group">
                <label>Target Exam <span class="required-mark">*</span></label>
                <select id="f_specific" required>
                  <option value="">Select</option>
                  <option value="IBPS PO">IBPS PO</option>
                  <option value="IBPS Clerk">IBPS Clerk</option>
                  <option value="SBI PO">SBI PO</option>
                  <option value="SBI Clerk">SBI Clerk</option>
                  <option value="RBI Grade B">RBI Grade B</option>
                  <option value="NABARD">NABARD</option>
                  <option value="Other Banking">Other Banking</option>
                </select>
                <div class="error-msg"></div>
              </div>
              <div class="input-group">
                <label>Target Post</label>
                <input type="text" id="f_institution" placeholder="e.g. Probationary Officer">
              </div>
            </div>
            <div class="input-group">
              <label>Gender</label>
              <select id="f_gender">
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>"""
    },
    {
        "filename": "state-exams.html",
        "title": "State Exams Application",
        "pill": "State Level Exams",
        "exam_name": "State Competitive Exam Coaching",
        "course_id": "state-exam",
        "category": "ssc",
        "specific": """
            <div class="form-row">
              <div class="input-group">
                <label>State <span class="required-mark">*</span></label>
                <select id="f_institution" required>
                  <option value="">Select</option>
                  <option value="Telangana">Telangana (TSPSC)</option>
                  <option value="Andhra Pradesh">Andhra Pradesh (APPSC)</option>
                  <option value="Other">Other state</option>
                </select>
                <div class="error-msg"></div>
              </div>
              <div class="input-group">
                <label>Exam Name <span class="required-mark">*</span></label>
                <input type="text" id="f_specific" placeholder="e.g. Group I, Group II, Group IV, SI" required>
                <div class="error-msg"></div>
              </div>
            </div>
            <div class="input-group">
              <label>Gender</label>
              <select id="f_gender">
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>"""
    },
    {
        "filename": "degree.html",
        "title": "Degree (UG) Admission Application",
        "pill": "Undergraduate Admission",
        "exam_name": "Degree (UG) Admission Guidance",
        "course_id": "degree-bcom",
        "category": "degree",
        "specific": """
            <div class="form-row">
              <div class="input-group">
                <label>Degree Course <span class="required-mark">*</span></label>
                <select id="f_specific" required>
                  <option value="">Select</option>
                  <option value="B.Com (General)">B.Com (General)</option>
                  <option value="B.Com (Honours)">B.Com (Honours)</option>
                  <option value="BBA">BBA</option>
                  <option value="BA">BA</option>
                  <option value="B.Sc">B.Sc</option>
                  <option value="Other">Other</option>
                </select>
                <div class="error-msg"></div>
              </div>
              <div class="input-group">
                <label>Preferred University</label>
                <input type="text" id="f_institution" placeholder="e.g. Osmania University">
              </div>
            </div>
            <div class="input-group">
              <label>Gender</label>
              <select id="f_gender">
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>"""
    },
    {
        "filename": "pg.html",
        "title": "Postgraduate (PG) Admission Application",
        "pill": "Postgraduate Admission",
        "exam_name": "PG (Postgraduate) Admission Guidance",
        "course_id": "pg-mba",
        "category": "pg",
        "specific": """
            <div class="form-row">
              <div class="input-group">
                <label>PG Course <span class="required-mark">*</span></label>
                <select id="f_specific" required>
                  <option value="">Select</option>
                  <option value="MBA">MBA</option>
                  <option value="M.Com">M.Com</option>
                  <option value="MA">MA</option>
                  <option value="M.Sc">M.Sc</option>
                  <option value="Other PG">Other PG</option>
                </select>
                <div class="error-msg"></div>
              </div>
              <div class="input-group">
                <label>Preferred University / College</label>
                <input type="text" id="f_institution" placeholder="e.g. Osmania, EFLU, HCU">
              </div>
            </div>
            <div class="input-group">
              <label>Gender</label>
              <select id="f_gender">
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>"""
    },
]

for form in FORMS:
    html = build_form(
        form["filename"], form["title"], form["pill"],
        form["exam_name"], form["course_id"], form["category"],
        form["specific"]
    )
    path = os.path.join(FORMS_DIR, form["filename"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ Generated: {form['filename']}")

print("\\nAll 11 forms generated.")
