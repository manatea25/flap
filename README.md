# FLAP - Feel Like A Pro

Перша в Україні мобільна платформа для футболістів-аматорів, що поєднує відео-челенджі, матчмейкінг та справедливу систему рейтингів.

## Функціональність

- ✅ Авторизація та реєстрація користувачів
- ✅ Створення профілю з детальною інформацією
- ✅ Система рейтингів (0.0-5.0)
- ✅ Внутрішня економіка з монетами
- ✅ Профілі гравців з контактами та статистикою
- ✅ Навігація між екранами з збереженням стану

## Технології

- Frontend: Flutter 3.x
- Backend: Firebase (Auth, Firestore, Storage)
- State Management: Provider
- UI: Material Design, Google Fonts

## Екрани

1. WelcomeScreen — головний екран
2. LoginScreen — вхід з валідацією
3. RegisterScreen — реєстрація
4. ProfileCreationScreen — створення профілю
5. HomeScreen — головна з навігацією

## Швидкий старт

### 1. Клонування
```bash
git clone https://github.com/manatea25/flap.git
cd flap
```

### 2. Встановлення залежностей
```bash
flutter pub get
```

### 3. Налаштування Firebase
1. Створіть проєкт у Firebase Console
2. Додайте додаток (Android/iOS/Web)
3. Додайте ключі у `lib/firebase_options.dart`

### 4. Запуск
```bash
flutter run
```

## Структура
```
lib/
├── main.dart
├── firebase_options.dart
├── services/
│   └── auth_service.dart
└── screens/
    ├── welcome_screen.dart
    ├── login_screen.dart
    ├── register_screen.dart
    ├── profile_creation_screen.dart
    └── home_screen.dart
```

## Примітки
- Для Android/iOS додайте відповідні `google-services.json`/`GoogleService-Info.plist`
- У файлі `firebase_options.dart` тимчасові плейсхолдери — замініть на ваші ключі
