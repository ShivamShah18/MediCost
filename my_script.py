import pandas as pd

def process_input(input1, input2, input3):
    # Read the Excel sheet into a Pandas DataFrame
    df = pd.read_excel('inputData.xlsx')
    
    # Filter the DataFrame for procedures containing the input1 string, ignoring case
    filtered_df = df[df['Procedure'].str.contains(input1, case=False, na=False) & (df['State'] == input2)]
    
    # Convert the 'Total' column to numeric, removing any non-numeric characters like '$' and ','
    filtered_df['Total'] = filtered_df['Total'].replace('[\$,]', '', regex=True).astype(float)
    
    # Calculate the average cost of the procedure for the specified state
    average_cost = filtered_df['Total'].mean()
    
    # Convert input3 to a float after removing non-numeric characters
    input_cost = float(input3)
    
    # Compare the input cost to the average cost
    if input_cost < average_cost:
        comparison_result = 'less than'
    elif input_cost > average_cost:
        comparison_result = 'greater than'
    else:
        comparison_result = 'equal to'
    
    # Return the result
    tableResult = createTable(input1, input2)
    
    return f"The cost of {input1} in {input2} is {comparison_result} the average cost. (Average: ${average_cost:,.2f}, Your Input: ${input_cost:,.2f}) \n\n {tableResult}"

def createTable(procedureInput, stateInput):
    file_path = "inputDataCSV.csv"
    df = pd.read_csv(file_path)
    df = df.loc[:, "Procedure": "Total"]
    df = df[df["Procedure"].str.contains(procedureInput, case=False, na=False)]
    df = df[df["State"] == stateInput]
    return df
