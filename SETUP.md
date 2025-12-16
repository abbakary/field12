# SITMS - Smart Industrial Training Matching System
## Setup Guide

### Problem Overview
The system was failing with the error:
```
WARNING Student registration invalid: {
  'institution': ['Invalid pk "1" - object does not exist.'],
  'course': ['Invalid pk "1" - object does not exist.']
}
```

This occurred because:
1. The database didn't have any Institution or Course records
2. The Flutter app was hardcoding institution_id=1 and course_id=1
3. The registration serializer was trying to validate foreign keys that didn't exist

### Solution Implemented

#### 1. Backend Setup (Django)

**Step 1: Create Management Command**
A new Django management command `seed_data` was created to populate the database with realistic data:
- 5 Tanzanian institutions (universities and technical institutes)
- Multiple departments per institution
- 20+ courses across departments
- 40+ skills (technical, soft, languages, management)

**Step 2: Run Database Seeding**
```bash
cd /workspace
python manage.py migrate
python manage.py seed_data
```

This command creates:
- **Institutions**: University of Dar es Salaam, MUST (Arusha), MBEYA MUST, Tanzania Institute of Technology, DIT
- **Departments**: Faculty of Engineering, IT, Science, Business, etc.
- **Courses**: Civil Engineering, Computer Science, Business Administration, IT, etc.
- **Skills**: Python, Java, JavaScript, Communication, Project Management, etc.

#### 2. Flutter Frontend Updates

**Step 1: Create Institution Model**
- File: `flutterapp/lib/models/institution.dart`
- Defines Institution and Course data models with proper JSON serialization

**Step 2: Create Institution Provider**
- File: `flutterapp/lib/providers/institution_provider.dart`
- Fetches institutions and courses from the API
- Manages selection state
- Handles loading and error states

**Step 3: Update Login/Registration Screen**
- File: `flutterapp/lib/screens/login_screen.dart`
- Added dropdown menus for Institution and Course selection
- Added Academic Level dropdown (Diploma, Degree, Masters)
- Improved form validation
- Added confirm password field
- Fixed hardcoded institution/course IDs

**Step 4: Create Organization Registration Screen**
- File: `flutterapp/lib/screens/organization_registration_screen.dart`
- Allows organizations to register with detailed information
- Includes industry type, location, website, and description fields

**Step 5: Update Main Application**
- File: `flutterapp/lib/main.dart`
- Added InstitutionProvider to the MultiProvider list
- Ensures institution/course data is available throughout the app

### API Endpoints Used

**Authentication Endpoints:**
- `POST /api/auth/student-register/` - Student registration
- `POST /api/auth/organization-register/` - Organization registration (to be implemented)
- `POST /api/auth/login/` - User login
- `GET /api/auth/profile/` - Get current user profile

**Data Endpoints:**
- `GET /api/v1/institutions/` - List all institutions
- `GET /api/v1/courses/` - List all courses
- `GET /api/v1/courses/?department=<id>` - Filter courses by department
- `GET /api/v1/skills/` - List all available skills

### Registration Flow

#### Student Registration Flow:
1. User selects "Register" tab on login screen
2. Fills in personal information (name, email, phone, etc.)
3. Application fetches and displays available institutions
4. User selects their institution
5. Application fetches and displays available courses
6. User selects their course and academic level
7. User creates password and confirms it
8. System validates all fields and sends registration request
9. Backend validates foreign keys (institution and course exist)
10. User is registered and logged in automatically
11. Dashboard is displayed with student-specific options

#### Organization Registration Flow:
1. User navigates to organization registration screen
2. Fills in organization details (name, industry, location, etc.)
3. Creates password and confirms it
4. System validates all fields and sends registration request
5. Backend validates and creates organization
6. User is logged in and redirected to organization dashboard

### Database Seeding Data

**Example Institutions:**
- University of Dar es Salaam (University)
- Tanzania University of Science and Technology (University)
- Mbeya University of Science and Technology (University)
- Tanzania Institute of Technology (Technical Institute)
- Dar es Salaam Institute of Technology (Technical Institute)

**Example Courses:**
- Bachelor in Civil Engineering (48 months)
- Bachelor in Computer Science (48 months)
- Diploma in Web Development (24 months)
- Masters in Cybersecurity (24 months)
- And many more...

**Example Skills:**
- Technical: Python, Java, JavaScript, Docker, AWS, Machine Learning
- Soft: Leadership, Communication, Problem Solving, Teamwork
- Languages: English, Swahili, French, Spanish, Mandarin
- Management: Financial Management, HR Management, Risk Management

### Testing the Registration

**Manual Testing Steps:**

1. **Start the backend:**
   ```bash
   cd /workspace
   python manage.py runserver
   ```

2. **Start the Flutter app** with proper API configuration

3. **Test Student Registration:**
   - Open the app
   - Click "Register" tab
   - Fill in student information:
     - Name: John Doe
     - Email: john@example.com
     - Registration Number: REG0001
     - Phone: +255 712 345 678
     - Password: SecurePass123
   - Select institution from dropdown (e.g., "University of Dar es Salaam")
   - Select course from dropdown (e.g., "Computer Science")
   - Select academic level (e.g., "degree")
   - Click "Create Account"
   - Should successfully register and redirect to dashboard

4. **Test Organization Registration:**
   - Navigate to organization registration screen
   - Fill in organization details
   - Should successfully register

### Validation Rules

**Student Registration Validation:**
- All fields are required
- Email must be valid format
- Password must be at least 8 characters
- Passwords must match
- Registration number must be unique
- Institution must exist in database
- Course must exist in database
- Academic level must be: diploma, degree, or masters

**Course Requirements:**
- Courses are filtered by selected institution's departments
- Only active courses are displayed
- Course level must match academic level selection

### Error Handling

The system now properly handles:
- Network timeouts (30 second timeout)
- Invalid credentials (400 Bad Request)
- Non-existent foreign keys (validation errors)
- Missing required fields (form validation)
- Duplicate usernames/emails (serializer validation)

### Future Enhancements

1. **Image Upload**: Support for institution logos and student profile photos
2. **Skills Selection**: Allow students to select skills during registration
3. **Email Verification**: Send verification emails during registration
4. **Organization Verification**: Admin approval process for organizations
5. **Two-Factor Authentication**: Additional security for sensitive operations
6. **Batch Import**: Admin tool to import institutions and courses from CSV

### Troubleshooting

**Issue**: "Institution not found" error
- **Solution**: Run `python manage.py seed_data` to populate the database

**Issue**: Empty institution dropdown
- **Solution**: Check API connectivity and ensure seed_data command completed successfully

**Issue**: "Passwords do not match"
- **Solution**: Ensure password and confirm password fields are identical

**Issue**: Network timeout during registration
- **Solution**: Check backend is running and accessible from the app

### Files Modified

**Backend:**
- `tracker/management/commands/seed_data.py` (NEW)
- `tracker/management/__init__.py` (NEW)
- `tracker/management/commands/__init__.py` (NEW)

**Frontend:**
- `flutterapp/lib/models/institution.dart` (UPDATED)
- `flutterapp/lib/providers/institution_provider.dart` (NEW)
- `flutterapp/lib/screens/login_screen.dart` (COMPLETELY REWRITTEN)
- `flutterapp/lib/screens/organization_registration_screen.dart` (NEW)
- `flutterapp/lib/main.dart` (UPDATED)

### Next Steps

1. **Run database seeding** on your development/production environment
2. **Test the registration flow** thoroughly
3. **Deploy the updated Flutter app** with the new registration screen
4. **Monitor for errors** in initial user registrations
5. **Gather feedback** and make improvements as needed
