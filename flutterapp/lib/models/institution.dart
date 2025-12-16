class Institution {
  final int id;
  final String name;
  final String institutionType;
  final String location;
  final String description;
  final String phone;
  final String email;
  final String website;
  final bool isActive;

  Institution({
    required this.id,
    required this.name,
    required this.institutionType,
    required this.location,
    required this.description,
    required this.phone,
    required this.email,
    required this.website,
    required this.isActive,
  });

  factory Institution.fromJson(Map<String, dynamic> json) {
    return Institution(
      id: json['id'] ?? 0,
      name: json['name'] ?? '',
      institutionType: json['institution_type'] ?? '',
      location: json['location'] ?? '',
      description: json['description'] ?? '',
      phone: json['phone'] ?? '',
      email: json['email'] ?? '',
      website: json['website'] ?? '',
      isActive: json['is_active'] ?? true,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'institution_type': institutionType,
      'location': location,
      'description': description,
      'phone': phone,
      'email': email,
      'website': website,
      'is_active': isActive,
    };
  }
}

class Course {
  final int id;
  final String name;
  final String code;
  final int department;
  final String departmentName;
  final String level;
  final String description;
  final int durationMonths;
  final bool isActive;

  Course({
    required this.id,
    required this.name,
    required this.code,
    required this.department,
    required this.departmentName,
    required this.level,
    required this.description,
    required this.durationMonths,
    required this.isActive,
  });

  factory Course.fromJson(Map<String, dynamic> json) {
    return Course(
      id: json['id'] ?? 0,
      name: json['name'] ?? '',
      code: json['code'] ?? '',
      department: json['department'] ?? 0,
      departmentName: json['department_name'] ?? '',
      level: json['level'] ?? '',
      description: json['description'] ?? '',
      durationMonths: json['duration_months'] ?? 0,
      isActive: json['is_active'] ?? true,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'code': code,
      'department': department,
      'department_name': departmentName,
      'level': level,
      'description': description,
      'duration_months': durationMonths,
      'is_active': isActive,
    };
  }
}
