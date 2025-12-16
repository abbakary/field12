from django.core.management.base import BaseCommand
from django.utils import timezone
from tracker.models import Institution, Department, Course, Skill


class Command(BaseCommand):
    help = 'Seed the database with initial institutions, departments, courses, and skills'

    def handle(self, *args, **options):
        self.stdout.write('Starting database seeding...')

        # ============================================================================
        # SEED INSTITUTIONS
        # ============================================================================
        institutions_data = [
            {
                'name': 'University of Dar es Salaam',
                'type': 'university',
                'location': 'Dar es Salaam',
                'phone': '+255 22 2668888',
                'email': 'info@udsm.ac.tz',
                'website': 'https://www.udsm.ac.tz',
                'description': 'Leading university in Tanzania offering bachelor and masters programs'
            },
            {
                'name': 'Tanzanias University of Science and Technology',
                'type': 'university',
                'location': 'Arusha',
                'phone': '+255 27 2544409',
                'email': 'info@must.ac.tz',
                'website': 'https://www.must.ac.tz',
                'description': 'Science and technology focused university'
            },
            {
                'name': 'Mbeya University of Science and Technology',
                'type': 'university',
                'location': 'Mbeya',
                'phone': '+255 25 2620090',
                'email': 'info@mbeya.ac.tz',
                'website': 'https://www.mbeya.ac.tz',
                'description': 'University specializing in engineering and technology'
            },
            {
                'name': 'Tanzania Institute of Technology',
                'type': 'technical',
                'location': 'Dar es Salaam',
                'phone': '+255 22 2862626',
                'email': 'info@tanza-tech.ac.tz',
                'website': 'https://www.tanza-tech.ac.tz',
                'description': 'Technical institute for vocational and technical training'
            },
            {
                'name': 'Dar es Salaam Institute of Technology',
                'type': 'technical',
                'location': 'Dar es Salaam',
                'phone': '+255 22 2131400',
                'email': 'info@dit.ac.tz',
                'website': 'https://www.dit.ac.tz',
                'description': 'Provides technical education in IT and engineering'
            },
        ]

        institutions = {}
        for inst_data in institutions_data:
            inst, created = Institution.objects.get_or_create(
                name=inst_data['name'],
                defaults={
                    'institution_type': inst_data['type'],
                    'location': inst_data['location'],
                    'phone': inst_data['phone'],
                    'email': inst_data['email'],
                    'website': inst_data['website'],
                    'description': inst_data['description'],
                    'is_active': True,
                }
            )
            institutions[inst_data['name']] = inst
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created institution: {inst.name}'))
            else:
                self.stdout.write(f'Institution already exists: {inst.name}')

        # ============================================================================
        # SEED DEPARTMENTS
        # ============================================================================
        departments_data = {
            'University of Dar es Salaam': [
                {'name': 'Faculty of Engineering', 'head': 'Prof. John Doe'},
                {'name': 'Faculty of Science', 'head': 'Prof. Jane Smith'},
                {'name': 'Faculty of Business', 'head': 'Prof. Robert Johnson'},
                {'name': 'Faculty of Arts', 'head': 'Prof. Mary Williams'},
                {'name': 'Faculty of IT', 'head': 'Prof. Michael Brown'},
            ],
            'Tanzanias University of Science and Technology': [
                {'name': 'Department of Engineering', 'head': 'Dr. Ahmed Hassan'},
                {'name': 'Department of Computing', 'head': 'Dr. Fatima Ali'},
                {'name': 'Department of Agriculture', 'head': 'Dr. Hassan Muhammad'},
            ],
            'Mbeya University of Science and Technology': [
                {'name': 'Department of Civil Engineering', 'head': 'Prof. David Wilson'},
                {'name': 'Department of Mechanical Engineering', 'head': 'Prof. Susan Davis'},
                {'name': 'Department of Electrical Engineering', 'head': 'Dr. Peter Miller'},
            ],
            'Tanzania Institute of Technology': [
                {'name': 'Technical Training Center', 'head': 'Eng. Tom Johnson'},
                {'name': 'Vocational Programs', 'head': 'Eng. Alice Lee'},
            ],
            'Dar es Salaam Institute of Technology': [
                {'name': 'IT Department', 'head': 'Dr. James White'},
                {'name': 'Engineering Department', 'head': 'Eng. Paul Green'},
            ],
        }

        departments = {}
        for inst_name, depts in departments_data.items():
            institution = institutions[inst_name]
            for dept_data in depts:
                dept, created = Department.objects.get_or_create(
                    institution=institution,
                    name=dept_data['name'],
                    defaults={
                        'head_of_department': dept_data['head'],
                        'is_active': True,
                    }
                )
                dept_key = f"{inst_name}::{dept_data['name']}"
                departments[dept_key] = dept
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created department: {dept.name}'))
                else:
                    self.stdout.write(f'Department already exists: {dept.name}')

        # ============================================================================
        # SEED COURSES
        # ============================================================================
        courses_data = {
            'University of Dar es Salaam::Faculty of Engineering': [
                {'name': 'Civil Engineering', 'code': 'CE-001', 'level': 'degree', 'duration': 48},
                {'name': 'Mechanical Engineering', 'code': 'ME-001', 'level': 'degree', 'duration': 48},
                {'name': 'Electrical Engineering', 'code': 'EE-001', 'level': 'degree', 'duration': 48},
            ],
            'University of Dar es Salaam::Faculty of Science': [
                {'name': 'Computer Science', 'code': 'CS-101', 'level': 'degree', 'duration': 48},
                {'name': 'Physics', 'code': 'PH-101', 'level': 'degree', 'duration': 48},
                {'name': 'Chemistry', 'code': 'CH-101', 'level': 'degree', 'duration': 48},
                {'name': 'Mathematics', 'code': 'MA-101', 'level': 'degree', 'duration': 48},
            ],
            'University of Dar es Salaam::Faculty of Business': [
                {'name': 'Business Administration', 'code': 'BA-101', 'level': 'degree', 'duration': 48},
                {'name': 'Accounting', 'code': 'ACC-101', 'level': 'degree', 'duration': 48},
                {'name': 'Marketing', 'code': 'MKT-101', 'level': 'degree', 'duration': 48},
            ],
            'University of Dar es Salaam::Faculty of IT': [
                {'name': 'Information Technology', 'code': 'IT-101', 'level': 'degree', 'duration': 48},
                {'name': 'Software Engineering', 'code': 'SE-101', 'level': 'degree', 'duration': 48},
                {'name': 'Cyber Security', 'code': 'CS-102', 'level': 'masters', 'duration': 24},
            ],
            'Tanzanias University of Science and Technology::Department of Engineering': [
                {'name': 'Mechanical Engineering', 'code': 'ME-MUST-001', 'level': 'degree', 'duration': 48},
                {'name': 'Civil Engineering', 'code': 'CE-MUST-001', 'level': 'diploma', 'duration': 36},
            ],
            'Tanzanias University of Science and Technology::Department of Computing': [
                {'name': 'Computer Engineering', 'code': 'CE-MUST-002', 'level': 'degree', 'duration': 48},
                {'name': 'Information Systems', 'code': 'IS-MUST-001', 'level': 'degree', 'duration': 48},
            ],
            'Mbeya University of Science and Technology::Department of Civil Engineering': [
                {'name': 'Civil Engineering', 'code': 'CE-MBEYA-001', 'level': 'degree', 'duration': 48},
                {'name': 'Construction Management', 'code': 'CM-MBEYA-001', 'level': 'diploma', 'duration': 36},
            ],
            'Mbeya University of Science and Technology::Department of Electrical Engineering': [
                {'name': 'Electrical Engineering', 'code': 'EE-MBEYA-001', 'level': 'degree', 'duration': 48},
                {'name': 'Power Systems', 'code': 'PS-MBEYA-001', 'level': 'masters', 'duration': 24},
            ],
            'Tanzania Institute of Technology::Technical Training Center': [
                {'name': 'Welding and Fabrication', 'code': 'WF-TIT-001', 'level': 'diploma', 'duration': 24},
                {'name': 'Automotive Technology', 'code': 'AT-TIT-001', 'level': 'diploma', 'duration': 24},
                {'name': 'Electrical Installation', 'code': 'EI-TIT-001', 'level': 'diploma', 'duration': 24},
            ],
            'Dar es Salaam Institute of Technology::IT Department': [
                {'name': 'Web Development', 'code': 'WD-DIT-001', 'level': 'diploma', 'duration': 24},
                {'name': 'Database Administration', 'code': 'DBA-DIT-001', 'level': 'diploma', 'duration': 24},
                {'name': 'Network Administration', 'code': 'NA-DIT-001', 'level': 'diploma', 'duration': 24},
            ],
        }

        for dept_key, courses in courses_data.items():
            department = departments[dept_key]
            for course_data in courses:
                course, created = Course.objects.get_or_create(
                    code=course_data['code'],
                    defaults={
                        'name': course_data['name'],
                        'department': department,
                        'level': course_data['level'],
                        'duration_months': course_data['duration'],
                        'is_active': True,
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created course: {course.name}'))
                else:
                    self.stdout.write(f'Course already exists: {course.name}')

        # ============================================================================
        # SEED SKILLS
        # ============================================================================
        skills_data = [
            # Technical Skills
            {'name': 'Python Programming', 'category': 'technical'},
            {'name': 'Java Programming', 'category': 'technical'},
            {'name': 'JavaScript', 'category': 'technical'},
            {'name': 'C++ Programming', 'category': 'technical'},
            {'name': 'SQL Database', 'category': 'technical'},
            {'name': 'Web Development', 'category': 'technical'},
            {'name': 'Mobile App Development', 'category': 'technical'},
            {'name': 'Cloud Computing', 'category': 'technical'},
            {'name': 'AWS', 'category': 'technical'},
            {'name': 'Docker', 'category': 'technical'},
            {'name': 'Machine Learning', 'category': 'technical'},
            {'name': 'Data Analysis', 'category': 'technical'},
            {'name': 'Cybersecurity', 'category': 'technical'},
            {'name': 'Network Administration', 'category': 'technical'},
            {'name': 'Linux System Administration', 'category': 'technical'},
            {'name': 'AutoCAD', 'category': 'technical'},
            {'name': 'MATLAB', 'category': 'technical'},
            {'name': 'Graphic Design', 'category': 'technical'},
            
            # Soft Skills
            {'name': 'Team Leadership', 'category': 'soft'},
            {'name': 'Communication', 'category': 'soft'},
            {'name': 'Problem Solving', 'category': 'soft'},
            {'name': 'Critical Thinking', 'category': 'soft'},
            {'name': 'Project Management', 'category': 'soft'},
            {'name': 'Time Management', 'category': 'soft'},
            {'name': 'Teamwork', 'category': 'soft'},
            {'name': 'Adaptability', 'category': 'soft'},
            {'name': 'Creativity', 'category': 'soft'},
            {'name': 'Customer Service', 'category': 'soft'},
            {'name': 'Negotiation', 'category': 'soft'},
            {'name': 'Conflict Resolution', 'category': 'soft'},
            
            # Languages
            {'name': 'English', 'category': 'language'},
            {'name': 'Swahili', 'category': 'language'},
            {'name': 'French', 'category': 'language'},
            {'name': 'Spanish', 'category': 'language'},
            {'name': 'Mandarin Chinese', 'category': 'language'},
            
            # Management Skills
            {'name': 'Financial Management', 'category': 'management'},
            {'name': 'Human Resource Management', 'category': 'management'},
            {'name': 'Quality Management', 'category': 'management'},
            {'name': 'Risk Management', 'category': 'management'},
            {'name': 'Strategic Planning', 'category': 'management'},
        ]

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={
                    'category': skill_data['category'],
                    'is_active': True,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created skill: {skill.name}'))
            else:
                self.stdout.write(f'Skill already exists: {skill.name}')

        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!'))
