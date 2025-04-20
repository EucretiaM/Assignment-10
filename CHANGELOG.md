# Changelog

## [1.0.0] - 2025-04-19

### Added

#### Design Patterns Implementation:
- `simple_factory.py` for assessment creation with `AssessmentFactory`.
- `factory_method.py` for notification sending (`EmailNotificationSender` and `InAppNotificationSender`).
- `abstract_factory.py` for UI theme management (`EducatorUIFactory` and `LearnerUIFactory`).
- `builder.py` for report generation (`ReportBuilder`).
- `prototype.py` for assessment template cloning (`AssessmentTemplate`).
- `singleton.py` for shared database connection (`DatabaseConnection`).

#### Test Cases:
- `test_simple_factory.py` for testing `AssessmentFactory`.
- `test_factory_method.py` for testing notification sending factories.
- `test_abstract_factory.py` for testing UI creation factories.
- `test_builder.py` for testing report building process.
- `test_prototype.py` for testing cloning of assessment templates.
- `test_singleton.py` for testing singleton database connection.

#### Module Initialization:
- Created `__init__.py` in the `creational_patterns` folder to expose all design patterns for centralized imports.

#### Class Diagram Implementation:
Implemented the class diagram in Python code to model user roles and entities in the system:
- **Base class**: `User` for common user properties and methods.
- **Subclasses**: `Learner` and `Educator` inheriting from `User`.

**Standalone classes** for key entities:
- `Assessment` for handling assessments.
- `Submission` for managing learner submissions.
- `Report` for generating educator reports.
- `Notification` for managing user notifications.
- `OTP` for handling one-time password verification.

### Changed
- Refactored the original design patterns into individual, modular files for better organization and maintainability.

### Fixed
- Enhanced modularity by separating each class and test pattern into standalone files.
- Improved usability and extensibility by centralizing imports in the `creational_patterns/__init__.py`.

Sure, here's the updated `CHANGELOG.md` with version numbers:

---

# CHANGELOG

## [1.0.0] - 2025-04-21

### Added
- **Simple Factory for Assessment Creation**
  - Implemented `AssessmentFactory` to handle assessment creation logic.
  - Returns `QuizAssessment` and `WrittenAssessment`.
  - **Rationale:** Encapsulates conditional logic and simplifies object creation for assessments.
  - **Status:** ✅ Resolved 

- **Factory Method for Notification Sending**
  - Implemented `NotificationSender` with subclasses `EmailNotificationSender` and `InAppNotificationSender`.
  - **Rationale:** Allows flexibility to support multiple notification types and makes it easy to extend by adding new types of notifications without modifying the base `NotificationSender`.
  - **Status:** ✅ Resolved 

- **Abstract Factory for UI Theme Management**
  - Implemented `EducatorUIFactory` and `LearnerUIFactory` to provide `Dashboard` and `Button`.
  - **Rationale:** Ensures a cohesive set of UI components tailored to the user role, making the code modular and reducing coupling between the components.
  - **Status:** ✅ Resolved 

- **Builder for Report Generation**
  - Implemented `ReportBuilder` to construct reports with sections like `Top Performers` and `Average Scores`.
  - **Rationale:** Provides a step-by-step mechanism to compose report sections in a controlled manner, eliminating the need for constructors with long parameter lists.
  - **Status:** ✅ Resolved 

- **Prototype for Assessment Templates**
  - Implemented `AssessmentTemplate` that can be cloned.
  - **Rationale:** Allows educators to clone a pre-existing template instead of re-creating it from scratch, saving time and ensuring consistency.
  - **Status:** ✅ Resolved 

- **Singleton for Database Connection**
  - Implemented `DatabaseConnection` to ensure only one instance is created and shared across the application.
  - **Rationale:** Ensures proper behavior in multi-threaded environments and avoids resource-intensive multiple connections.
  - **Status:** ✅ Resolved 

