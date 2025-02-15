# Mouad Garroud
from fpdf import FPDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style="", size=12)

summary_text = """Mouad Garroud

**Summary of XML Document**

# **Page 1: Introduction to XML**

### **1. Overview of XML**
- XML (eXtensible Markup Language) is a standard for structuring data.
- It is a subset of SGML (Standard Generalized Markup Language) and was standardized by W3C in 1998.
- XML is not a programming language but a meta-language for defining markup languages.

### **2. Key Features of XML**
- **Human-Readable & Self-Descriptive**: Designed for easy interpretation.
- **Structured Format**: Uses a tree structure for organizing data.
- **Universal & Portable**: Supports Unicode and can be used across different platforms.
- **Extensible**: Users define their own tags to suit their needs.

### **3. Comparison with Other Markup Languages**
- **XML vs HTML**: HTML is for presentation; XML is for data storage and exchange.
- **XML vs SGML**: XML is simpler and easier to use than SGML.

# **Page 2: Structure and Components of XML Documents**

### **1. Composition of an XML Document**
- **Prologue**: Specifies XML version, encoding, and standalone status.
  - Example: `<?xml version="1.0" encoding="UTF-8" standalone="no"?>`
- **Processing Instructions**: Optional commands for applications processing XML.
- **Root Element**: The single, top-level element that contains all other elements.
- **Elements & Attributes**: Define structure and additional information.
- **Entities**: Used for reusable components within XML.

### **2. Well-Formed vs Valid XML**
- **Well-formed**: Properly structured (tags are nested and closed correctly).
- **Valid**: Follows a predefined structure defined by a DTD or XML Schema.

# **Page 3: Document Type Definitions (DTD) & XML Schema**

### **1. Role of DTD**
- Defines the grammar and structure of an XML document.
- Specifies valid elements, attributes, and their relationships.
- Can be internal (within the XML file) or external (referenced from another file).

### **2. DTD Example**
```xml
<!ELEMENT commission (personne+)>
<!ELEMENT personne (nom, prenom?, email*)>
<!ATTLIST personne fonction (president | tresorier | membre) #REQUIRED>
```

### **3. XML Schema**
- More powerful than DTD and written in XML.
- Supports data types (integer, string, date, etc.).
- Example of XML Schema:
```xml
<xs:element name="personne">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="nom" type="xs:string"/>
      <xs:element name="prenom" type="xs:string" minOccurs="0"/>
      <xs:element name="email" type="xs:string" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

# **Page 4: XML Presentation & Data Processing**

### **1. XML Styling with XSLT and CSS**
- **CSS**: Can be used to style XML for web display.
- **XSLT (eXtensible Stylesheet Language Transformations)**: Converts XML into other formats (HTML, text, PDF).
- Example XSLT Code:
```xml
<xsl:template match="/">
  <html>
    <body>
      <xsl:for-each select="commission/personne">
        <p><xsl:value-of select="nom"/> <xsl:value-of select="prenom"/></p>
      </xsl:for-each>
    </body>
  </html>
</xsl:template>
```

### **2. XML Parsing Techniques**
- **SAX (Simple API for XML)**: Event-driven, memory-efficient parsing.
- **DOM (Document Object Model)**: Loads entire XML into memory for easy manipulation.
- **Data Binding**: Maps XML directly to objects in programming languages (Java, Python, etc.).

# **Page 5: Advanced XML Concepts & Applications**

### **1. XML Namespaces**
- Prevents conflicts when combining multiple XML vocabularies.
- Example:
```xml
<book xmlns="http://www.example.com/books" xmlns:pub="http://www.example.com/publisher">
  <title>XML Guide</title>
  <pub:publisher>O'Reilly</pub:publisher>
</book>
```

### **2. XML Querying & Databases**
- **XPath**: Extracts data from XML documents using path expressions.
  - Example: `/commission/personne[nom='Thierry']`
- **XQuery**: SQL-like queries for XML databases.
- **XML Databases**: Stores structured XML data for efficient retrieval.

### **3. UML & XML Integration**
- **XMI (XML Metadata Interchange)**: Standard for exchanging UML models in XML format.
- **Use in Web & Business Applications**:
  - Web Services (SOAP, REST APIs)
  - Data Exchange (RSS, SVG, MathML)
  - Configuration Files (Android, Java, .NET settings)

---

This summary provides a structured breakdown of XML, focusing on its essentials, structure, validation, styling, and practical applications. Let me know if you need further details or modifications!



"""
for line in summary_text.split("\n"):
    pdf.cell(0, 8, line, ln=True)
pdf_filename = "XML_Summary.pdf"
pdf.output(pdf_filename)
pdf_filename