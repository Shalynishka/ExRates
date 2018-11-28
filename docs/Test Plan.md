
1. [Introduction](#1) <br> 
2. [Test Items](#2) <br>
3. [Risk Issues](#3) <br>
4. [Features to Test](#4) <br>
5. [Test Approach](#5) <br>
6. [Pass/Fail Criteria](#6) <br>
7. [Conclusion](#7) <br>

# 1. Introduction <a name = "1"></a>

This document represent the Test Plan developed for the mobile application ExRates.
The main aim of testing – verification of the functionality and validation of work of the application.


# 2. Test Items <a name = "2"></a>

The ExRates is created to simplify working with rates in everyday life. It uses NBRB and cryptocompare API to get necessary information.

**Quality attributes (ISO 25010):**

1. Functional Suitability
	- Functional completeness;
	- Functional correctness;
	- Functional appropriateness.
2. Usability 
	- Operability.
	- User error protection.
	- User interface aesthetics.
	- Accessibility.

# 3. Risk Issues <a name = "3"></a>

- Not enough space to store application data;
- Discontinue API support.


# 4. Features to Test <a name = "4"></a>
	
During testing process planned to check correctness of implementation followed main functionality:
	
- **Getting rates**
	1. Getting current rates.
	2. Getting last rates with no Internet.
- **Selection of important currencies**
	1. Addition of selected currencies
	2. Deletion of selected currencies
- **Searching currencies**
	1. Full name search
	2. Partial name search
- **Currencies converter**
   This use case should be tested on:
	1. Offline conversion
	2. Conversion Accuracy

It is also important to check correctness of non-functional requirements:

- Usability: All elements must have restrained tones and must be readable..
- Reliability of information: The product must provide the most current information on the exchange rate and resources.

# 5. Test Approach <a name = "5"></a>

This application will be tested manually.

# 6. Pass/Fail Criteria <a name = "6"></a>

Results of testing are represented in this [document](https://github.com/Shalynishka/ExRates/blob/master/docs/Test%20Results.md).

# 7. Conclusion <a name = "7"></a>

The test plan allows to test the main functionality of the ExRates application. Successful passing of all tests does not guarantee full operability. Nevertheless, this is an indication that the work is done.

