# Inventory Management System

This project is an Inventory Management System that allows users to manage supplier details efficiently. It provides functionalities to add, update, delete, search, and display supplier information.

## Files in the Project

- **supplier.py**: This file contains the `SupplierClass`, which manages supplier details in the inventory management system. It includes methods for adding, updating, deleting, searching, and displaying supplier information. The class interacts with an SQLite database to perform these operations.

- **ims.db**: This is the SQLite database file that stores supplier information. It contains a table named `supplier` with the following columns:
  - `invoice`: The invoice number of the supplier (Primary Key).
  - `name`: The name of the supplier.
  - `contact`: The contact information of the supplier.
  - `description`: A description of the supplier.

## Setup Instructions

1. **Clone the Repository**: 
   Clone this repository to your local machine using the following command:
   ```
   git clone <repository-url>
   ```

2. **Install Required Packages**: 
   Ensure you have Python installed on your machine. You may need to install the `Pillow` library for image handling:
   ```
   pip install pillow
   ```

3. **Database Setup**: 
   The `ims.db` file is included in the project. Ensure that it is in the root directory of the project. The database contains the necessary table for managing suppliers.

4. **Run the Application**: 
   Navigate to the `PRESENTATION` directory and run the `supplier.py` file:
   ```
   python supplier.py
   ```

## Usage

- Upon running the application, a GUI will appear where you can enter supplier details.
- Use the "Save" button to add a new supplier.
- You can update or delete existing suppliers by searching for their invoice number.
- The application will display all suppliers in a table format.

## License

This project is open-source and available for use and modification.