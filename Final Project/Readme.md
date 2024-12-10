<div align="center">
<img src = "https://github.com/user-attachments/assets/c5b3a24c-bafa-470c-b509-6231bcc2c132" alt="Alt text" />
</div>


### **I. A Brief Project Overview**  
This program is an **Apartment Reservation System** designed to help users view available apartments, make reservations, update or delete bookings, and manage reservations efficiently. It stores apartment details and reservations in a **SQLite database**, ensuring data persistence across sessions. The project aims to simplify apartment hunting and reservation processes while promoting sustainability by encouraging efficient resource use and urban development.

---

### **II. Explanation of How Python Concepts, Libraries, and OOP Principles Were Applied**  

#### **Python Concepts**  
1. **File I/O**: SQLite database is used for persistent data storage, allowing seamless access and updates.  
2. **Error Handling**: Input validation ensures users provide correct data (e.g., date format, valid apartment IDs).  
3. **Datetime Module**: Ensures proper handling of reservation dates and times.  

#### **Python Libraries**  
- **SQLite3**: Provides a lightweight, file-based database for storing apartment and reservation information.  
- **Datetime**: Validates and formats reservation dates for accurate handling.  

#### **OOP Principles**  
1. **Encapsulation**:  
   - Classes like `Apartment` and `Reservation` bundle data (attributes) and operations (methods) into single units.  
   - `ApartmentFinder` and `ReservationManager` encapsulate database operations, abstracting away the complexity.  

2. **Abstraction**:  
   - Database initialization and query execution details are hidden inside helper classes like `ApartmentFinder`.  
   - Users only interact with higher-level methods like `add_apartment` or `make_reservation`.  

3. **Polymorphism**:  
   - The `__str__` method in `Apartment` and `Reservation` provides custom string representations, enabling object descriptions suited for the context.  

4. **Responsibility Segregation**:  
   - **`ApartmentFinder`** manages apartment-related operations.  
   - **`ReservationManager`** handles reservation tasks.  
   - **`Apartment` and `Reservation`** represent data entities, focusing on their specific details.  

---

### **III. Details of the Chosen SDG and Its Integration into the Project**  

#### **Sustainable Development Goal (SDG): Goal 11 - Sustainable Cities and Communities**  
This project aligns with **SDG 11**, which focuses on creating inclusive, safe, and sustainable cities. The integration includes:  
- **Efficient Urban Development**: By helping individuals find apartments that meet their budget, location, and amenity needs, it promotes efficient housing allocation.  
- **Data-Driven Decisions**: The database structure ensures data transparency, enabling users to select accommodations based on amenities like eco-friendly facilities.  
- **Scalable Design**: The project can be extended to include environmental sustainability metrics (e.g., energy-efficient apartments).  

---

### **IV. Instructions for Running the Program**  

1. **Requirements**:  
   - Python 3.x  
   - SQLite (built into Python, no additional installation required)  

2. **Setup**:  
   - Copy the program code into a Python script file (e.g., `apartment_reservation.py`).  
   - Run the script using the command:  
     ```bash
     python apartment_reservation.py
     ```  

3. **Program Navigation**:  
   - **Main Menu Options**:  
     1. View available apartments (displays apartments with details like location, price, and amenities).  
     2. Make a reservation (requires apartment ID and reservation date).  
     3. View reservations (lists all active bookings).  
     4. Update reservation (modify customer name, apartment ID, or date).  
     5. Delete reservation (remove existing reservations by ID).  
     6. Exit (ends the program).  

4. **Sample Data**:  
   - Sample apartments are pre-loaded into the database. Additional apartments can be added using the `add_apartment` method in `ApartmentFinder`.  

5. **Future Extensions**:  
   - Add environmental metrics for apartments (e.g., energy efficiency, green certifications).  
   - Allow users to filter apartments based on sustainability features.  

This structure makes the program practical for real-world use while also adhering to sustainability goals.
