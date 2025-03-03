data_processing_constitution = """

Introduction  

This constitution defines how to transform dataset column descriptions into structured First-Order Logic (FOL) predicates.  
The goal is to create a well-defined representation of dataset attributes to facilitate structured knowledge extraction and reasoning.  

---

Definitions  
- Dataset Column: A named attribute in the dataset with a description and data type.  
- Predicate: A logical statement capturing information about a dataset column.  
- Column Predicate Definition: A predicate representing a column's name, data type, and description.  
- Column Relationship Predicate: A predicate defining how two or more dataset columns relate to each other.  

---

 Predicates for Column Representation  

1. Entity Definition Predicates  
   - `HasValueRange(ColumnName, MinValue, MaxValue)` → Defines the valid range for numeric columns.  
   - `HasUnit(ColumnName, UnitType)` → Specifies the measurement unit.  
   - `HasCategories(ColumnName, [Category1, Category2, ...])` → Defines possible categorical values.  

2. Column Relationship Predicates  
   - `Describes(Entity, ColumnName)` → Indicates the entity that a column describes.  
   - `RelatedTo(ColumnA, ColumnB, RelationshipType)` → Defines a dependency between columns.  

3. Semantic Representation Predicates  
   - `Represents(ColumnName, Concept)` → Defines the high-level concept of the column.  
   - `Measures(ColumnName, Subject, Property)` → Specifies what a column measures.  

---

 Transformation Rules  
1. Extract Metadata: Identify column names, data types, and descriptions.  
2. Apply Predicates: Assign relevant predicates based on column properties.  
3. Ensure Completeness: Capture all dataset attributes accurately.  
4. Handle Special Cases: Process missing values, categories, and units.  

---

 Example Transformation  

# Input (Column Descriptions Format)  

{
    "id": {"description": "Unique numerical identifier of the dataset entry.", "data_type": "integer"},
    "compound_name": {"description": "Name of the drug or compound used in the lifespan-extending study.", "data_type": "string"},
    "species": {"description": "The species of the model organism in which the lifespan-extending study was conducted.", "data_type": "string"},
    "strain": {"description": "The specific strain of the model organism used in the study.", "data_type": "string"},
    "dosage": {"description": "The dosage of the drug or compound administered to the model organism in the study.", "data_type": "string"},
    "age_at_initiation": {"description": "The age of the model organism at the start of the treatment with the drug or compound.", "data_type": "float"},
    "treatment_duration": {"description": "The duration for which the model organism was treated with the drug or compound.", "data_type": "float"}
}


Output (Generated Predicates)


Represents("compound_name", "Drug Name")  
Represents("species", "Model Organism")  
Represents("strain", "Organism Strain")  
Represents("dosage", "Treatment Dosage")  
Represents("age_at_initiation", "Age at Treatment Start")  
Represents("treatment_duration", "Treatment Duration")  

Measures("age_at_initiation", "Organism", "Age")  
Measures("treatment_duration", "Treatment", "Duration")  
HasUnit("age_at_initiation", "Years")  
HasUnit("treatment_duration", "Days")  



 Implementation Guidelines  
 Accuracy: Precisely capture all details of the study.  
 Comprehensiveness: Include all available information.  
 Clarity: Maintain clear and understandable predicate expressions.  

"""