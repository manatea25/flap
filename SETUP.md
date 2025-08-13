# Швидке налаштування FLAP

## Кроки
1. `flutter pub get`
2. Налаштуйте Firebase ключі у `lib/firebase_options.dart`
3. Для Android/iOS додайте `google-services.json`/`GoogleService-Info.plist`
4. `flutter run`

## Структура
```
lib/
  main.dart
  firebase_options.dart
  services/auth_service.dart
  screens/
    welcome_screen.dart
    login_screen.dart
    register_screen.dart
    profile_creation_screen.dart
    home_screen.dart
```