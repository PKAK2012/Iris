# Iris

This dataset is used to identify the species type based on the other features provided in the columns.

Column description:
sepal_length  - Describes the sepal_length of the species
sepal_width   - Describes the sepal_width of the species
petal_length  - Describes the petal_length of the species
petal_width   - Describes the petal_width of the species
petal_width   - Describes the petal_width of the species
species       - Descibes the species type

Data Preprocessing:
There are no spelling mistakes or null values in the dataset.
Only one column, species, has an object datatype. This column was converted to an integer datatype using the Ordinal Encoder.

Before Data Cleaning:
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object 

After Data Cleaning:
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    float64

Conclusion:
The Iris dataset is well-prepared for machine learning tasks after the necessary data preprocessing steps. With no missing values or spelling mistakes, and all columns properly encoded, this dataset is suitable for supervised learning classification tasks. 
It can be effectively used to classify species types based on sepal and petal dimensions.



 
