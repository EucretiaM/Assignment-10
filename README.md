# Math Booster - Assignment 10

[Programming language choice and key decisions](#programming-language-choice-and-key-decisions)

## Design Patterns and Their Justifications

### Simple Factory (`AssessmentFactory`)
**Justification:**  
The Simple Factory pattern is ideal for scenarios where the creation process depends on a specific type. In this case, the need to create different types of assessments (`QuizAssessment` or `WrittenAssessment`) based on a single input (`type_`) makes the Simple Factory a natural choice. It encapsulates object creation logic, ensuring that calling code is not cluttered with conditionals or instantiations, promoting clean and maintainable code.

---

### Factory Method (`NotificationSender`)
**Justification:**  
The Factory Method pattern is suitable for creating objects while deferring the exact type to subclasses. For sending notifications, it allows flexibility to support multiple notification types (`EmailNotificationSender` and `InAppNotificationSender`). The pattern makes it easy to extend by adding new types of notifications (e.g., SMS) without modifying the base `NotificationSender`, adhering to the Open-Closed Principle.

---

### Abstract Factory (`EducatorUIFactory` and `LearnerUIFactory`)
**Justification:**  
The Abstract Factory pattern is used to create families of related objects without specifying their concrete classes. In the context of UI theme management, educators and learners require distinct but consistent UI elements (e.g., `Dashboard` and `Button`). This pattern ensures that a factory can provide a cohesive set of UI components tailored to the user role, making the code modular and reducing coupling between the components.

---

### Builder (`ReportBuilder`)
**Justification:**  
The Builder pattern is excellent for constructing complex objects with multiple optional steps. Reports can have varying content (e.g., top performers, average scores), and the Builder pattern provides a step-by-step mechanism to compose these sections in a controlled manner. This eliminates the need for constructors with long parameter lists and makes the report generation process more readable and flexible.

---

### Prototype (`AssessmentTemplate`)
**Justification:**  
The Prototype pattern is used when creating a new object is resource-intensive, and we want to clone existing objects instead. For reusable assessment templates, the pattern allows educators to clone a pre-existing template (`AssessmentTemplate`) instead of re-creating it from scratch. This saves time and ensures consistency when working with predefined structures.

---

### Singleton (`DatabaseConnection`)
**Justification:**  
The Singleton pattern ensures that only one instance of a class is created and shared across the application. A database connection is a perfect use case, as creating multiple connections is resource-intensive, and a single, shared connection instance suffices. This implementation also demonstrates thread safety, ensuring proper behavior in multi-threaded environments.

---

### Summary
By leveraging these patterns in their respective scenarios, the code achieves **modularity**, **scalability**, and adherence to software design principles like:
- **Open-Closed Principle**
- **Single Responsibility Principle**
- **Separation of Concerns**

### Programming language choice and key decisions

####  Why Python?

Python was chosen for its:

- **Simplicity & Readability** – Easy translation from UML to code with minimal syntax overhead.  
- **Rapid Prototyping** – Ideal for fast development and iteration on design patterns.  
- **Strong Testing Support** – Tools like `pytest` and `pytest-cov` enable clean, efficient testing and coverage reporting.  
- **Community & Ecosystem** – Wide support for CI/CD, design pattern demos, and educational use cases.

---

####  Key Design Choices

- **Clear Pattern Separation** – Each creational pattern is isolated in its own module.  
- **UML Alignment** – Classes directly reflect the Mermaid class diagram.  
- **CI-Ready** – Includes GitHub Actions + Codecov integration for automated testing and reporting.
