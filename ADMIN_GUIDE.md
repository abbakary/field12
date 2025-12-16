# SITMS Admin Panel Guide

## Overview

The SITMS Admin Panel has been completely configured to provide comprehensive management of all system processes, including institutions, students, organizations, training opportunities, applications, and more.

## Accessing the Admin Panel

1. **Navigate to**: `http://your-domain/admin/`
2. **Login** with your Django superuser credentials
3. You will see: **SITMS Administration Portal**

## Admin Panel Features

### 1. Institution Management

**Location**: Admin Home → Institutions

**Features:**
- View all educational institutions
- Add new institutions with type (University, College, Technical Institute)
- Manage institution details (location, contact info, website)
- View count of active departments
- Filter by type or location
- Search by name, location, or email
- Activate/deactivate institutions in bulk
- View creation and update timestamps

**Key Actions:**
- ✅ Mark selected as active
- ❌ Mark selected as inactive

**Display Fields:**
- Institution Name
- Type (University/College/Technical)
- Location
- Number of Active Departments
- Status (Active/Inactive)
- Created Date

---

### 2. Department Management

**Location**: Admin Home → Departments

**Features:**
- View all departments within institutions
- Add departments with head of department information
- Track course count per department
- Filter by institution or status
- Search by name or department head
- Bulk status management

**Key Information:**
- Department name and institution
- Head of department name
- Number of active courses
- Activity status

---

### 3. Course Management

**Location**: Admin Home → Courses

**Features:**
- Manage all academic courses/programs
- Course details: Code, Level (Diploma/Degree/Masters), Duration
- Link courses to departments and institutions
- Filter by level, institution, or status
- Search by course name or code
- Ensure unique course codes

**Academic Levels:**
- Diploma (typically 24-36 months)
- Bachelor Degree (typically 48 months)
- Masters (typically 24 months)

---

### 4. Skill Management

**Location**: Admin Home → Skills

**Features:**
- Manage skills database
- Track students with each skill
- Categorize skills: Technical, Soft Skills, Languages, Management
- View number of students per skill
- Activate/deactivate skills for use in applications

**Skill Categories:**
- **Technical**: Python, Java, JavaScript, Docker, AWS, Machine Learning, etc.
- **Soft Skills**: Leadership, Communication, Teamwork, Problem Solving, etc.
- **Languages**: English, Swahili, French, Spanish, Mandarin, etc.
- **Management**: Financial, HR, Quality, Risk Management, etc.

---

### 5. Student Management

**Location**: Admin Home → Students

**Features:**
- Complete student profile management
- View/edit registration details
- Manage institution and course assignments
- Track placement status and placement dates
- Manage student skills (multi-select)
- Upload student profile photos
- View student contact information
- Filter by institution, course, academic level, or placement status
- Search by name, email, or registration number

**Key Student Information:**
- Full Name and Email (from User)
- Registration Number (unique)
- Institution and Course
- Academic Level
- Contact Phone and Preferred Location
- Profile Photo and Bio
- Skills (multi-select)
- Placement Status (placed/not placed)
- Placement Date
- Registration Date

**Student Display Format:**
- Shows all skills as colorful tags
- Indicates placement status clearly
- Quick access to all student details

---

### 6. Organization Management

**Location**: Admin Home → Organizations

**Features:**
- Manage partner organizations
- Verification workflow (pending/verified)
- Track ratings and review counts
- Monitor active training opportunities
- Manage supported courses and required skills
- Filter by verification status, location, or industry
- Search by name, industry, or email

**Organization Actions:**
- ✅ Verify selected organizations
- ❌ Unverify selected organizations
- Activate/deactivate organizations

**Key Information:**
- Organization name and industry type
- Location and contact details
- Verification status and verified by admin
- Rating and review count
- Number of active training opportunities
- Supported courses and required skills

**Verification Process:**
- Admins can mark organizations as verified
- Automatically records verification admin and timestamp
- Only verified organizations show on student browsing lists (configurable)

---

### 7. Training Opportunity Management

**Location**: Admin Home → Training Opportunities

**Features:**
- Create and manage training opportunities
- Track available slots and filled slots
- Manage deadlines
- Set requirements: minimum GPA, supported levels, skills
- Specify supported courses
- Monitor number of applications
- View opportunity status (open/closed)

**Opportunity Details:**
- Title and Organization
- Total slots and remaining slots
- Filled slots indicator
- Training duration in months
- Minimum GPA requirement
- Supported academic levels (Diploma/Degree/Both)
- Required skills (multi-select)
- Supported courses (multi-select)
- Application deadline
- Open/closed status

**Status Indicators:**
- Shows filled slots with color indicator (red for high fill)
- Shows total applications count
- Automatic closure when slots are full

---

### 8. Application Management

**Location**: Admin Home → Applications

**Features:**
- Monitor all student applications
- View matching information and scores
- Manage application status (pending/accepted/rejected)
- Track application timeline
- Bulk acceptance/rejection
- View status change history (inline)
- Add acceptance letters or rejection reasons
- Specify training start/end dates

**Application Status:**
- Pending (awaiting decision)
- Accepted (student approved)
- Rejected (student not selected)
- Withdrawn (student withdrew)
- Completed (training completed)

**Key Information:**
- Student and Organization
- Training Opportunity
- Match Quality (High/Medium/Low/Not Eligible)
- Match Score (0-100%)
- Match Details breakdown
- Status and dates
- Acceptance/rejection information

**Bulk Actions:**
- Accept multiple applications at once
- Reject multiple applications at once

**Status History:**
- Inline view of all status changes
- Track who made changes and when
- View change notes

---

### 9. Notification Management

**Location**: Admin Home → Notifications

**Features:**
- View system notifications (read-only)
- Monitor notification delivery
- Filter by type and read status
- Search by title or message
- Track notification timestamps

**Notification Types:**
- Application Received
- Application Accepted
- Application Rejected
- New Opportunity Posted
- Deadline Reminder
- System Message

**Note**: Notifications are auto-generated by system; admins can view but not create manually.

---

### 10. Review Management

**Location**: Admin Home → Reviews

**Features:**
- Monitor student reviews of organizations
- View ratings and comments
- Verify reviews
- Filter by rating or verification status
- Link reviews to completed applications

**Review Information:**
- Student and Organization
- Rating (1-5 stars with visual indicator)
- Title and Comment
- Verification status
- Related application

**Note**: Only students who completed training can leave reviews.

---

### 11. System Configuration

**Location**: Admin Home → System Configuration

**Features:**
- Configure system-wide settings
- Set values for:
  - Placement Year
  - Minimum GPA for placement
  - Application deadlines
  - Max applications per student
  - Notification settings

**Configuration Keys:**
- `placement_year`: Current year for placement tracking
- `min_gpa`: Minimum GPA requirement
- `application_deadline`: Deadline for applications
- `max_applications_per_student`: Limit applications per student
- `notification_enabled`: Enable/disable notifications

---

## Common Admin Tasks

### Task 1: Add a New Institution

1. Go to **Institutions**
2. Click **+ Add Institution**
3. Fill in:
   - Name: e.g., "University of Dar es Salaam"
   - Type: Select from dropdown
   - Location: City/Region
   - Description: Optional
   - Contact: Email, Phone, Website
4. Click **Save**

### Task 2: Create Courses for Institution

1. Go to **Departments**
2. Click **+ Add Department**
3. Select Institution and enter Department name
4. Go to **Courses**
5. Click **+ Add Course**
6. Link to the department created above
7. Set course code, level, and duration

### Task 3: Verify an Organization

1. Go to **Organizations**
2. Select organizations to verify from the list
3. Click **Verify selected organizations** dropdown action
4. Click **Go**
5. Organization will be marked as verified with timestamp

### Task 4: Manage Training Opportunity

1. Go to **Training Opportunities**
2. Create or edit opportunity
3. Set:
   - Title and description
   - Total slots available
   - Supported courses and levels
   - Required skills
   - Application deadline
4. System automatically tracks remaining slots

### Task 5: Process Student Applications

1. Go to **Applications**
2. Filter by status = "pending"
3. For each application:
   - Click to open
   - Review match score and details
   - Add acceptance letter OR rejection reason
   - Set status to "accepted" or "rejected"
   - Add training dates if accepted
4. Or use bulk actions:
   - Select multiple pending applications
   - Choose "Accept selected applications"
   - Click **Go**

### Task 6: Monitor System Health

**Key Dashboard Views:**

Check statistics:
- **Students**: Total registered and placed
- **Organizations**: Verified vs unverified count
- **Opportunities**: Open vs closed, slots available
- **Applications**: Pending vs completed
- **Notifications**: Unread count

### Task 7: Configure System Settings

1. Go to **System Configuration**
2. Add or edit configuration values:
   ```
   Key: placement_year
   Value: 2024
   ```
3. Click **Save**

---

## Admin Permissions & Security

### Role-Based Access:

**Superuser (Full Access):**
- Can view, create, edit, delete all records
- Can verify organizations
- Can approve applications
- Can manage system configuration

**Staff User (Limited Access):**
- Configure permissions in Django user management
- Can restrict certain models or actions
- Can set read-only fields

### Best Practices:

1. **Regular Audits**: Review verification requests weekly
2. **Application Management**: Process pending applications regularly
3. **System Monitoring**: Check notification delivery and error logs
4. **Data Integrity**: Ensure unique registration numbers and course codes
5. **Backup**: Regular database backups before major changes

---

## Filtering & Search Tips

### Filter by Multiple Criteria:

**Example: Find all pending applications from a specific organization**
1. Go to Applications
2. Click **Filter by Status**: Select "Pending"
3. Click **Filter by Organization**: Select organization name
4. View filtered results

### Advanced Search:

**Example: Find all students from specific institution not yet placed**
1. Go to Students
2. Type institution name in search box
3. Filter by **is_placed**: "No"
4. View results

---

## Dashboard Overview

When you log into the admin panel, you'll see:

- **Recent Actions**: Your admin activity log
- **Application Counts**: Stats on students, orgs, opportunities
- **Quick Links**: Navigate to each section
- **Module Listing**: All manageable models

---

## Troubleshooting

### Issue: Can't verify organization
- **Check**: User has staff permissions
- **Solution**: Go to User management, ensure user is staff/superuser

### Issue: Application status not updating
- **Check**: Status field is not read-only in your edit form
- **Solution**: Ensure you're using the correct status values

### Issue: Notifications not showing
- **Check**: `notification_enabled` in System Configuration
- **Solution**: Enable notifications in System Configuration

### Issue: Can't delete Institution with courses
- **Check**: Institution has related courses/departments
- **Solution**: First delete all courses, then departments, then institution

---

## Customization Options

The admin panel is highly customizable. Potential enhancements:

1. **Custom Filters**: Add complex filtering logic
2. **Export Data**: Add CSV export for reports
3. **Custom Actions**: Add workflow actions like "Send Notification"
4. **Charts/Reports**: Add dashboard with analytics
5. **Inline Editing**: Allow editing in list view
6. **Admin Dashboard**: Create custom dashboard with key metrics

---

## Support & Feedback

For admin panel issues or feature requests, contact the development team.

**Key Documentation Files:**
- `SETUP.md` - Initial setup instructions
- `ADMIN_GUIDE.md` - This file
- Django Admin Docs: https://docs.djangoproject.com/en/stable/ref/contrib/admin/
