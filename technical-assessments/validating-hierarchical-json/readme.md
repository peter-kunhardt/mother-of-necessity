# Analytics Engineer Technical Case
**Data Cleaning, Warehouse Schema Design**

## Assignment Description
A fintech company receives complex JSON objects representing balance sheets from partner orgs and needs a way of validating and storing the data for analysis.

A JSON file is provided describing a balance sheet. ("assets", "liabilities", "equity") This is representative of data received from partner orgs.

Our objective is two-fold:
1) Design a data model to retain the information in the warehouse for analysis
2) Validate that the file to be imported is accurate ($ amounts listed in each nodes should sum to the value of their parent node, values are represented in appropriate types)

The validation solution is designed to be executed as part of a pipeline that can help populate the `is_validated` and `validation_errors` columns in the raw data table from our ERD, so the file returns `is_validated` (bool) and `validation_errors` (object) in a way that is optimized for machine use rather than human eyes.

## Ideation:
### 1) Data Modeling:
We are asked to provide an ERD as the main deliverable. While there are a few reference architectures one can use for importing JSON to a warehouse environment, in this case I will assume we are doing something like:

Land data in S3 in raw JSON > load to warehouse in a "raw" table with just PK, time of insert, result of our validation check, and a JSON column > transform with dbt. 

I'll make the ERD to reflect the "raw" table, staging tables, and data marts.

### 2) Data Validation:
Validation can theoretically occur at several different stages of this process depending on how the data is usually ingested. If data is uploaded by partners manually, it may be useful to have a script to validate contents that can be run the moment the upload occurs so we can pass an error to the user. For this project, I'll make a python script that performs the validation and returns a boolean `passed_validation` value and a summary of errors that could be included in the raw table in the warehouse.

### Assumptions:
1) The hierarchy depth of the JSON file may be arbitrary.
2) All imports in this format will have exactly three top level nodes, always called "assets", "liabilities", and "equity".
3) Only leaf nodes (the line items) have account_id values.

### Future Changes:
#### In ERD/transformation solution:
1) Provider partner shouldn't be a varchar, there should be a separate table of provider partners. It might already exist elsewhere in the schema, or we may need to update it dynamically.
2) Do we need to retain a table of account IDs, or even display them in our data marts? These may refer to IDs of records in a partner's warehouse and therefore may not be useful to our analysts.
3) Liability groups are not reflected in this dataset but they might be in the future. I also wanted to make it simple for users to know that they have to connect the full chain. We would probably instantiate an equity_group with an `equity_group_name` of 'NONE' or leave Null to indicate there isn't really a group.
4) Some of these columns may be "overnamed" > if it's on the `liability_groups` table it's usually safe to assume a `value` is the value of the liability group in question. This is a matter of style, I just wanted to go for maximum clarity in this case.
5) Handling new hierarchy designs: this system would not tolerate subgroups of line items or new types of balance sheet categories outside assets/liabilities/equity. I've assumed this is a tool for importing balance sheets only, but if that's not true we need to adjust the ERD accordingly.
6) If we are transacting very large numbers of these balance sheets regularly, we might consider using JSONB and making the import statement more interpretive rather than importing straight text from the original file.

#### In validation solution:
1) Errors are a little duplicative; you get extra reports when a number is not a decimal since it doesn't break out of the for: very intelligently. We could manipulate the order of operations and put in some smart `return` statements to cut down on that duplicativeness.
2) If we want to produce an error log more legible to humans we could add some `print()` statements. 
