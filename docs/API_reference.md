The `API_reference.md` should provide detailed information about the project's modules, classes, functions, and their respective usage. Here’s a structure you can follow:

#### 1. Introduction
Provide a brief overview of the API reference, explaining its purpose and how it can help developers understand the internal workings of the project.


# API Reference

This document provides detailed information about the modules, classes, and functions used in the "Ransomware Simulation and Defense" project. It is intended for developers looking to understand the internal workings and extend the functionality of the project.


#### 2. Modules Overview
List the main modules in the project with a brief description of each.


## Modules Overview

- simulation: Contains the core functionality for simulating ransomware attacks.
- defense: Includes tools for backup management, decryption, and ransomware detection.
- utils: Provides utility functions and logging capabilities.


#### 3. Class and Method Descriptions

For each class, include the following details:

- Class Name
- Description: What the class does.
- Constructor: Parameters and their descriptions.
- Methods: Detailed descriptions of each method, including parameters and return types.

##### Example


### Class:FileEncryptor

Description: This class handles file encryption and decryption using symmetric encryption (Fernet).

Constructor:
- FileEncryptor(key=None): Initializes the `FileEncryptor` with a given key. If no key is provided, a new key is generated.
  - key (bytes): A bytes object representing the encryption key. If `None`, a new key is generated.

Methods:
- encrypt_file(file_path): Encrypts the specified file.
  - file_path (str): The path to the file to encrypt.
  - Returns: None
  
- decrypt_file(file_path): Decrypts the specified file.
  - file_path (str): The path to the file to decrypt.
  - Returns: None

- get_key(): Returns the encryption key used by the encryptor.
  - Returns: byte