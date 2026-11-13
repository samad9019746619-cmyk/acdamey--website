# 🏛️ The Neo Global Educational Academy — Master Web Portal

Official modern web portal for **The Neo Global Educational Academy**, Hyderabad (Recognised by Govt. of Telangana, under the management of Millat Medical Educational Society).

Designed & Developed by **Mohammed Abdul Samad**.

---

## 📁 Project Folder Structure

```
academy-website/
├── index.html                   # Main student-facing portal with dedicated course application forms
├── admin.html                   # Authenticated Admin Application Management Dashboard
├── verify_upgrade.py            # Automated audit and verification test suite
├── netlify.toml                 # Netlify deployment and API routing configuration
│
├── images/                      # Official crest logo and 18 authentic campus event photos
│   ├── logo.jpeg                # Official crest of The Neo Global Educational Academy
│   └── 1.jpeg - 18.jpeg         # High-resolution convocation, classroom, and seminar photos
│
├── backend/                     # Python FastAPI Backend Architecture
│   ├── requirements.txt         # Backend Python dependencies
│   ├── .env.example             # Environment configuration template
│   ├── database.py              # SQLAlchemy engine and SQLite session dependency
│   ├── models.py                # Database models for Applications and Admin Users
│   ├── schemas.py               # Pydantic validation models for all 31 application fields
│   ├── auth.py                  # JWT authentication and bcrypt password hashing
│   ├── seed.py                  # Database table creation and default admin seed script
│   ├── main.py                  # FastAPI application entry point with CORS & static mounting
│   └── routers/
│       ├── applications.py      # Public application submission & reference generation
│       ├── admin.py             # Admin login, search, filter, status update, and CSV export
│       └── courses.py           # Configurable course catalog and academic years
│
└── netlify/                     # Serverless Netlify Functions (Dual Deployment Compatibility)
    └── functions/
        └── send-whatsapp.js     # Serverless admission submission & CallMeBot WhatsApp alert
```

---

## 🚀 Step-by-Step Setup & Running in VS Code

### Option 1: Standalone Static Mode (Frontend Only)
1. Open the `academy-website` folder in **VS Code**.
2. Right-click `index.html` and select **"Open with Live Server"** (or double-click `index.html` to open in any web browser).
3. The website operates with local client-side storage and instant WhatsApp routing.

---

### Option 2: Full-Stack Mode (Python FastAPI + SQLite Backend)
1. Open a terminal in the project directory in VS Code:
   ```bash
   cd c:\Users\Dell\Desktop\academy-website
   ```
2. (Optional but recommended) Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   # On Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   ```
3. Install backend dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
4. Configure environment variables (optional, defaults are pre-configured):
   ```bash
   cp backend/.env.example backend/.env
   ```
5. Initialize the SQLite database and seed the default administrator:
   ```bash
   python -m backend.seed
   ```
6. Start the FastAPI development server:
   ```bash
   uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
   ```
7. Access the application:
   - **Student Portal**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - **Admin Portal**: [http://127.0.0.1:8000/admin.html](http://127.0.0.1:8000/admin.html)
   - **Interactive API Docs (Swagger)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **Health Check**: [http://127.0.0.1:8000/api/health](http://127.0.0.1:8000/api/health)

---

## 🔐 Admin Dashboard Credentials

- **URL**: `admin.html` (or `/admin.html` when served via backend)
- **Default Username**: `admin`
- **Default Password**: `NeoAcademy@2025`
*(Change the default password in `backend/.env` before deploying to production).*

### Admin Features:
- Real-time application metrics (Total, Pending, Approved, Enrolled).
- Live search by student name, application reference ID, or mobile number.
- Multi-filter by course, category, and status.
- Detailed modal inspecting all 31 submitted student, parent, academic, and document fields.
- Status updater (`Pending`, `Under Review`, `Approved`, `Enrolled`, `Rejected`) and counselor notes.
- One-click CSV export of all applications.

---

## 📞 Official Contact Numbers & WhatsApp Routing

- **Official Line 1**: `8019546619`
- **Official Line 2**: `9849822213`
- **Address**: Shah Ali Banda, Opp. Jannat The Designer Studio, Old City, Hyderabad.

### Post-Submission WhatsApp Behavior:
Upon submitting any course admission form:
1. Application is persisted to the database.
2. Unique Reference ID (`TNGA-YYYYMMDD-XXXX`) is issued.
3. Two distinct WhatsApp buttons are displayed:
   - **Send Admission Enquiry to 8019546619** (`https://wa.me/918019546619?text=...`)
   - **Send Admission Enquiry to 9849822213** (`https://wa.me/919849822213?text=...`)
4. WhatsApp message contains **ONLY safe summary data** (Ref Number, Student Name, Course, Batch, Contact). Sensitive identity documents, Aadhaar details, and residential addresses are **never** transmitted over WhatsApp.

---

## 📝 Dedicated Course Forms Included

Every course has its own identifiable form with course-specific headings, custom options, and validation:
1. **Intermediate MPC** (Maths, Physics, Chemistry + JEE Mains Foundation)
2. **Intermediate BiPC** (Biology, Physics, Chemistry + NEET Medical Foundation)
3. **Intermediate CEC** (Commerce, Economics, Civics + CA Foundation / CPT)
4. **Intermediate HEC** (History, Economics, Civics + Civil Services Foundation)
5. **NEET Preparation** (Long-term, intensive, and 100-day crash batches)
6. **IIT-JEE Preparation** (Mains & Advanced masterclasses)
7. **B.Com (General)**
8. **B.Com (Computer Applications)**
9. **BBA (Bachelor of Business Administration)**
10. **B.Sc (Physical Sciences - MPCs / MSCs)**
11. **B.Sc (Life Sciences - BZC / Biotech)**
12. **B.A (Humanities, Social Sciences & Media)**
13. **MBA (Finance, Marketing, HR, Systems)**
14. **M.Com (Advanced Accounting & Taxation)**
15. **M.Sc (Organic Chemistry / Comp Science)**
16. **M.A (Languages & Political Science)**
17. **Vocational MLT (Medical Laboratory Technology)**
18. **Vocational Physiotherapy & Rehabilitation**
19. **Vocational MPHW Nursing (Multipurpose Health Worker)**
20. **Pre-Primary / Teacher Training (PPTTC)**
21. **Job-Oriented Computer Science & Tech**
22. **Hifz Academy** (Dual memorization + formal board academics, Tajweed assessment)
23. **Class 10th / SSC Board Preparation**
24. **100 Days Fast Track Special Crash Course**
25. **Placement Assistance & Job Registration** (Tailored for job-seekers without redundant school parent fields)

---

## ⚙️ Adding or Modifying Courses

To modify or add courses to the catalog:
1. **Frontend**: Edit the `ALL_COURSES` array in `index.html`. Each entry supports `id`, `name`, `category`, `badge`, `duration`, `eligibility`, `desc`, `customLabel`, and `customOptions`.
2. **Backend**: Edit `COURSES_CATALOG` in `backend/routers/courses.py`.

---

## 🧪 Automated Testing & Verification

Run the automated verification suite to audit phone numbers, branding, section removal, and course triggers:
```bash
python verify_upgrade.py
```
Expected output:
- 0 occurrences of `6305625465` across all project files.
- Exact developer signature `Mohammed Abdul Samad` verified.
- Complete removal of `Hall of Fame / Voice of Our Achievers` verified.
- All 25 dedicated course triggers verified.

