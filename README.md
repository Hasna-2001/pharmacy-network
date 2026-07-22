# Pharmacy Network

A desktop application for managing an online pharmacy network, built with Python and CustomTkinter. It provides both a customer-facing storefront and an admin panel for managing pharmacies, doctors, and inventory.

## Features

- **User authentication** — sign in / sign up flow (`login.py`, `signin.py`, `cart_sign_in.py`)
- **Storefront / e-pharmacy** — browse drugs and categories such as baby care, skin care, and fitness products (`all_drugs.py`, `epharmacies.py`, `baby_care.py`, `skin_care.py`, `fitness.py`)
- **Cart & checkout** — shopping cart, shipping form, payment, and receipt generation (`cart.py`, `shippingform.py`, `payment.py`, `recipt.py`)
- **Order tracking** — view past orders (`my_orders.py`)
- **Nearby pharmacies** — locate pharmacies near the user (`nearby_pharmacy.py`)
- **Doctor listings** — view and manage doctor profiles (`doctors.py`, `doctor_form.py`)
- **Donations** — donate-to-a-cause flow (`donate_us.py`, `donate_payment.py`)
- **Feedback** — customer feedback form (`feedback.py`)
- **Admin panel** — add/remove pharmacies and doctors, manage offers and new items (`admin_panel_page.py`, `admin_add_pharmacy.py`, `admin_doctors_form.py`, `add_pharmacy_form.py`, `remove_pharmacy.py`, `remove_doctors.py`, `add_offers.py`, `new_item_add_form.py`)

## Tech Stack

- **Python 3**
- **tkinter** / **customtkinter** — GUI framework
- **CTkSpinbox** — custom spinbox widget for CustomTkinter
- **SQLite3** (`sqlite3`) — local database (`pharmacy.db`)
- **Pillow** (`PIL`) — image handling
- **functools**, **os** — standard library utilities

## Project Structure

```
pharmacy-network/
├── application/
│   ├── Pharmacy Network.exe    # Compiled Windows executable
│   ├── pharmacy.db             # SQLite database
│   └── retrieved_image.jpg
├── pharmacy_network Source Codes/
│   ├── main.py                 # Application entry point
│   ├── home.py, lobby.py       # Landing / home screens
│   ├── login.py, signin.py     # Authentication
│   ├── cart.py, payment.py, shippingform.py, recipt.py   # Checkout flow
│   ├── admin_*.py              # Admin panel screens
│   ├── *.png, *.jpg            # UI assets/icons
│   └── main.spec               # PyInstaller build spec
└── Required Libraries.txt
```

## Getting Started

### Prerequisites

Install the required libraries:

```bash
pip install customtkinter CTkSpinbox pillow
```

(`tkinter`, `sqlite3`, `functools`, and `os` ship with the Python standard library.)

### Running from source

```bash
cd "pharmacy_network Source Codes"
python main.py
```

### Running the compiled build

A prebuilt Windows executable is available at `application/Pharmacy Network.exe`, bundled with its `pharmacy.db` database.

## Notes

- The database file (`pharmacy.db`) contains the schema and data used by the app — keep it alongside the executable or source when running.
- `main.spec` is the PyInstaller spec file used to produce the standalone `.exe` build.
