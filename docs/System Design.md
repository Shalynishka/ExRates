
[Glossary](https://github.com/Shalynishka/ExRates/blob/master/docs/Glossary.md) <br>

1. [Use Case Diagram](#1) <br>
	1.1. [Actors](#1.1) <br> 
	1.2. [Use Cases](#1.2) <br>
		1.2.1. [Check favorites](#1.2.1) <br>
		1.2.2. [Update](#1.2.2) <br>
    1.2.3. [Check all](#1.2.3) <br>
    1.2.4. [Find currency](#1.2.4) <br>
    1.2.5. [Check resources](#1.2.5) <br>
    1.2.6. [Check crypts](#1.2.6) <br>
    1.2.7. [Converter](#1.2.7) <br>
 2. [Activity Diagram](#2) <br>

# 1. Use Case Diagram <a name = "1"></a>

<p align = "center">
<img width = "1178" height = "797" src="https://github.com/Shalynishka/ExRates/blob/master/Diagrams/Use%20case.png">
</p>

## 1.1 Actors <a name = "1.1"></a>

Actor | Desription
:-----|:----------
User  | A person who use an application
Bank  | Bank which provides api

## 1.2 Use Cases <a name = "1.2"></a>

### 1.2.1 Check favorites <a name = "1.2.1"></a>

**Description**: Use Case "Check favorites" allows user to recieve information about favorites currencies. **Preconditions**: User opened the application.
Flow of events: 

1. If application hasn't connection to the Internet, alternate flow A1 is running;
2. Updating information about favorite currencies;
3. Application shows currencies;
4. End.

### 1.2.2 Update <a name = "1.2.2"></a>

**Description**: Use Case "Update" updates information about currencies and resources. **Preconditions**: User pressed "Update" icon.
Flow of events: 

1. Application cheks connection to the Internet. If no connection, alternate flow A1 is running. When an error occurs, error flow E1 is running;
2. Application updates data;
3. End.

### 1.2.3 Check all <a name = "1.2.3"></a>

**Description**: Use case "Check all" allows user to get information about all currencies. **Preconditions**: User selects "All currencies" menu.
Flow of events: 

1. If application hasn't connection to the Internet, alternate flow A1 is running;
2. Updating information about all currencies;
3. Application shows currencies;
4. End.

### 1.2.4 Find currency <a name = "1.2.4"></a>

**Description**: Use case "Find currency" allows user to find currency and get information about it. **Preconditions**: User selects "Find currency" menu.
Flow of events: 

1. User inputs short name or keyword of currency;
2. Application shows result of searching;
3. End.

### 1.2.5 Check resources <a name = "1.2.5"></a>

**Description**: Use case "Check resources" allows user to get information about resources. ****Preconditions**: User selects "Resources" menu.
Flow of events: 

1. If application hasn't connection to the Internet, alternate flow A1 is running;
2. Updating information about resources;
3. Application shows resources;
4. End.

### 1.2.6 Check crypts <a name = "1.2.6"></a>

**Description**: Use case "Check crypts" allows user to get information about crypts. **Preconditions**: User selects "Cryptocurrency" menu.
Flow of events: 

1. If application hasn't connection to the Internet, alternate flow A1 is running;
2. Updating information about crypts;
3. Application shows crypts;
4. End.
 
### 1.2.7 Converter <a name = "1.2.7"></a>

**Description**: Use case "Converter" allows user to convert currencies. **Preconditions**: User selects "Converter" menu.
Flow of events: 

1. User selects necessary currencies;
2. Application calculates values and shows them;
3. End.

# 2. Activity Diagram <a name = "2"></a>

When user selects menu "All currencies" an application checks Internet acces. In case of lack of access, the application uses saved information about currencies and display it. Otherwise the app updates data about currencies and display fresh information.

<p align = "center">
<img width = "1665" height = "789" src="https://github.com/Shalynishka/ExRates/blob/master/Diagrams/Activity.png">
</p>


