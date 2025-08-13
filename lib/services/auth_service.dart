import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class AuthService extends ChangeNotifier {
  final FirebaseAuth _auth = FirebaseAuth.instance;
  final FirebaseFirestore _firestore = FirebaseFirestore.instance;
  
  User? get currentUser => _auth.currentUser;
  bool get isLoggedIn => _auth.currentUser != null;
  
  Future<UserCredential?> registerWithEmailAndPassword({
    required String email,
    required String password,
    required String name,
    required String surname,
    required String city,
    required String age,
    required String position,
    required String experience,
  }) async {
    try {
      UserCredential userCredential = await _auth.createUserWithEmailAndPassword(
        email: email,
        password: password,
      );
      
      await _firestore.collection('users').doc(userCredential.user!.uid).set({
        'name': name,
        'surname': surname,
        'city': city,
        'age': age,
        'position': position,
        'experience': experience,
        'email': email,
        'createdAt': FieldValue.serverTimestamp(),
        'rating': 0.0,
        'coins': 100,
      });
      
      notifyListeners();
      return userCredential;
    } catch (e) {
      print('Помилка реєстрації: $e');
      return null;
    }
  }
  
  Future<UserCredential?> signInWithEmailAndPassword({
    required String email,
    required String password,
  }) async {
    try {
      UserCredential userCredential = await _auth.signInWithEmailAndPassword(
        email: email,
        password: password,
      );
      
      notifyListeners();
      return userCredential;
    } catch (e) {
      print('Помилка входу: $e');
      return null;
    }
  }
  
  Future<void> signOut() async {
    await _auth.signOut();
    notifyListeners();
  }
  
  Future<Map<String, dynamic>?> getUserProfile() async {
    if (currentUser == null) return null;
    
    try {
      DocumentSnapshot doc = await _firestore
          .collection('users')
          .doc(currentUser!.uid)
          .get();
      
      if (doc.exists) {
        return doc.data() as Map<String, dynamic>;
      }
      return null;
    } catch (e) {
      print('Помилка отримання профілю: $e');
      return null;
    }
  }
}