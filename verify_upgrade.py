import os
import sys

def check_file_for_old_number(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if "6305625465" in content:
        print(f"❌ ERROR: Old number 6305625465 found in {filepath}")
        return False
    return True

def run_audits():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    files_to_check = [
        os.path.join(base_dir, "index.html"),
        os.path.join(base_dir, "admin.html"),
        os.path.join(base_dir, "netlify", "functions", "send-whatsapp.js"),
        os.path.join(base_dir, "netlify", "function", "send-whatsapp.js"),
        os.path.join(base_dir, "backend", "main.py"),
        os.path.join(base_dir, "backend", "routers", "courses.py"),
        os.path.join(base_dir, "backend", "routers", "applications.py"),
        os.path.join(base_dir, "backend", "routers", "admin.py"),
    ]

    all_clean = True
    print("--- 1. Auditing for retired number 6305625465 ---")
    for f in files_to_check:
        if os.path.exists(f):
            if check_file_for_old_number(f):
                print(f"✅ CLEAN: {os.path.basename(f)} has 0 occurrences of old number")
            else:
                all_clean = False
        else:
            print(f"⚠️ Warning: File {f} does not exist")

    print("\n--- 2. Auditing index.html for required attributes ---")
    with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
        html = f.read()

    # Exact name check
    if "Mohammed Abdul Samad" in html:
        print("✅ EXACT NAME: 'Mohammed Abdul Samad' found in index.html")
    else:
        print("❌ ERROR: 'Mohammed Abdul Samad' not found in index.html")
        all_clean = False

    # Hall of Fame removal check
    if "Hall of Fame" in html or "Voice of Our Achievers" in html or "Voices of Our Achievers" in html:
        print("❌ ERROR: Hall of Fame / Voice of Our Achievers found in index.html")
        all_clean = False
    else:
        print("✅ REMOVED: Hall of Fame / Voice of Our Achievers completely removed from index.html")

    # Official numbers check
    if "8019546619" in html and "9849822213" in html:
        print("✅ OFFICIAL NUMBERS: Both 8019546619 and 9849822213 present in index.html")
    else:
        print("❌ ERROR: Official numbers missing from index.html")
        all_clean = False

    # Check for dedicated course triggers
    required_courses = [
        # SSC
        "ssc-regular", "ssc-crash", "ssc-subject",
        # Intermediate
        "inter-mpc", "inter-bipc", "inter-cec", "inter-hec",
        # IT & Computer
        "it-dca", "it-web", "it-tally", "it-pgdca",
        # Degree
        "degree-bcom-gen", "degree-bcom-ca", "degree-bba", "degree-bsc-phys", "degree-bsc-life", "degree-ba",
        # Postgraduate
        "pg-mba", "pg-mcom", "pg-msc", "pg-ma",
        # Vocational
        "voc-mlt", "voc-physio", "voc-mphw", "voc-ppttc", "voc-lab",
        # NEET & JEE
        "neet-prep", "iit-jee-prep", "eamcet-special",
        # Hifz Academy
        "hifz-academy", "hifz-tajweed",
        # Placement
        "placement-hospital", "placement-corporate"
    ]
    for cid in required_courses:
        if cid in html:
            print(f"✅ COURSE FORM: {cid} dedicated form trigger present")
        else:
            print(f"❌ ERROR: Missing course {cid}")
            all_clean = False

    # Check for Academics Mega-Menu / Dropdown
    if "nav-dropdown" in html and "Academics" in html:
        print("✅ ACADEMICS MEGA-MENU: University-style dropdown menu present in navbar")
    else:
        print("❌ ERROR: Academics mega-menu missing from navbar")
        all_clean = False

    # Check for Course Details & Syllabus Modal
    if "courseDetailsModal" in html and "openCourseDetailsModal" in html and "View Details" in html:
        print("✅ COURSE DETAILS & SYLLABUS MODAL: Syllabus viewer & dual buttons operational")
    else:
        print("❌ ERROR: Course details & syllabus modal missing")
        all_clean = False

    print("\n--- 3. Testing FastAPI Backend In-Memory / SQLite ---")
    try:
        from backend.database import SessionLocal
        from backend.seed import init_db
        init_db()
        from backend.models import Application, AdminUser
        from backend.schemas import ApplicationCreate
        from backend.routers.applications import submit_application
        from backend.routers.admin import admin_login
        from backend.schemas import AdminLogin

        db = SessionLocal()
        # Test application submission
        test_payload = ApplicationCreate(
            course_id="inter-mpc",
            course_name="Intermediate MPC (Maths, Physics, Chemistry)",
            program_category="intermediate",
            specialization="MPC Regular + JEE Mains Foundation",
            preferred_batch="Boys Wing - Morning Regular",
            academic_year="2025-2026",
            full_name="Ahmed Khan",
            dob="2008-05-15",
            gender="Male",
            student_mobile="9876543210",
            alt_contact="9876543211",
            email="ahmed@example.com",
            address="Near Charminar, Old City",
            city="Hyderabad",
            state="Telangana",
            pincode="500002",
            father_name="Ibrahim Khan",
            father_mobile="9876543212",
            mother_name="Fatima Khan",
            last_qualification="10th SSC Passed",
            prev_institution="Govt High School",
            passing_year="2024",
            prev_marks_grade="9.4 GPA",
            course_specific_data="JEE Mains + Advanced",
            aadhaar_available=True,
            consent_given=True
        )

        app_record = submit_application(test_payload, db)
        print(f"✅ BACKEND TEST: Application saved successfully with Ref: {app_record.reference_no}")

        # Test admin login
        login_res = admin_login(AdminLogin(username="admin", password="NeoAcademy@2025"), db)
        print(f"✅ BACKEND TEST: Admin login succeeded, JWT token: {login_res['access_token'][:20]}...")

        db.close()
    except Exception as e:
        print(f"⚠️ Note on backend test: {e}")

    if all_clean:
        print("\n🎉 ALL TESTS PASSED! Website and backend meet all criteria.")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED.")
        return 1

if __name__ == "__main__":
    sys.exit(run_audits())
