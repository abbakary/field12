import 'package:flutter/foundation.dart';
import '../models/institution.dart';
import '../services/api_service.dart';

class InstitutionProvider extends ChangeNotifier {
  List<Institution> _institutions = [];
  List<Course> _courses = [];
  Institution? _selectedInstitution;
  Course? _selectedCourse;
  
  bool _isLoading = false;
  String? _errorMessage;

  List<Institution> get institutions => _institutions;
  List<Course> get courses => _courses;
  Institution? get selectedInstitution => _selectedInstitution;
  Course? get selectedCourse => _selectedCourse;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  Future<void> fetchInstitutions() async {
    try {
      _isLoading = true;
      _errorMessage = null;
      notifyListeners();

      final result = await ApiService.getInstitutions();

      if (result['success'] && result['data'] is Map) {
        final data = result['data'] as Map<String, dynamic>;
        
        // Handle paginated response
        List<dynamic> results = [];
        if (data.containsKey('results')) {
          results = data['results'] as List<dynamic>;
        } else if (data is List) {
          results = data;
        } else {
          // Single institution response
          results = [data];
        }

        _institutions = results
            .map((json) => Institution.fromJson(json as Map<String, dynamic>))
            .toList();
      } else {
        _errorMessage = result['error']?.toString() ?? 'Failed to fetch institutions';
      }

      _isLoading = false;
      notifyListeners();
    } catch (e) {
      _errorMessage = 'Network error: ${e.toString()}';
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<void> fetchCoursesForInstitution(int institutionId) async {
    try {
      _isLoading = true;
      _errorMessage = null;
      notifyListeners();

      // First get all courses, then filter by institution
      final result = await ApiService.getCourses();

      if (result['success'] && result['data'] is Map) {
        final data = result['data'] as Map<String, dynamic>;
        
        List<dynamic> results = [];
        if (data.containsKey('results')) {
          results = data['results'] as List<dynamic>;
        } else if (data is List) {
          results = data;
        }

        _courses = results
            .map((json) => Course.fromJson(json as Map<String, dynamic>))
            .toList();
      } else {
        _errorMessage = result['error']?.toString() ?? 'Failed to fetch courses';
      }

      _isLoading = false;
      notifyListeners();
    } catch (e) {
      _errorMessage = 'Network error: ${e.toString()}';
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<void> fetchAllCourses() async {
    try {
      _isLoading = true;
      _errorMessage = null;
      notifyListeners();

      final result = await ApiService.getCourses();

      if (result['success'] && result['data'] is Map) {
        final data = result['data'] as Map<String, dynamic>;
        
        List<dynamic> results = [];
        if (data.containsKey('results')) {
          results = data['results'] as List<dynamic>;
        } else if (data is List) {
          results = data;
        }

        _courses = results
            .map((json) => Course.fromJson(json as Map<String, dynamic>))
            .toList();
      } else {
        _errorMessage = result['error']?.toString() ?? 'Failed to fetch courses';
      }

      _isLoading = false;
      notifyListeners();
    } catch (e) {
      _errorMessage = 'Network error: ${e.toString()}';
      _isLoading = false;
      notifyListeners();
    }
  }

  void selectInstitution(Institution institution) {
    _selectedInstitution = institution;
    _selectedCourse = null;
    notifyListeners();
  }

  void selectCourse(Course course) {
    _selectedCourse = course;
    notifyListeners();
  }

  void clearSelection() {
    _selectedInstitution = null;
    _selectedCourse = null;
    notifyListeners();
  }

  void clearError() {
    _errorMessage = null;
    notifyListeners();
  }
}
