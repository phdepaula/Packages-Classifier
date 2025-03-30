# 📦 Package Classifier for Dispatch Queue  

This project implements a **package classifier** based on its dimensions and mass, determining the appropriate dispatch stack.  

## 📌 **Package Classification**  

Packages are categorized according to the following criteria:  

- **🟢 STANDARD**: Packages that are **neither bulky nor heavy** can be handled normally.  
- **🟡 SPECIAL**: Packages that are **either bulky or heavy** cannot be handled automatically.  
- **🔴 REJECTED**: Packages that are **both bulky and heavy** are rejected.  

## ⚙️ **How It Works?**  

The classifier analyzes packages based on their **dimensions (height, width, and length) and mass**, determining the appropriate dispatch stack.  

💡 **Classification Rules:**  
- A package is **bulky** if its volume (**width × height × length**) is **≥ 1,000,000 cm³** or any of its dimensions is **≥ 150 cm**.  
- A package is **heavy** if its mass is **≥ 20 kg**.  
- A package is **rejected** if it is **both bulky and heavy**.  

## 🚀 **Technologies Used**  
- [**Python**](https://docs.python.org/3/)
- [**Pytest**](https://docs.pytest.org/en/stable/)

## 🛠 Setup & Installation  

### Create a Virtual Environment  
Run the following command in the project root folder:  

```sh
python -m venv venv
```

### Activate the Virtual Environment  
- **Windows:**  
  ```sh
  venv\Scripts\activate
  ```  
- **macOS/Linux:**  
  ```sh
  source venv/bin/activate
  ```  

### Install Dependencies  
Install all required dependencies from the `requirements.txt` file:  

```sh
pip install -r requirements.txt
```

### Run the Tests  
Execute the test suite using Pytest:  

```sh
pytest
```