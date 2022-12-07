import pandas as pd

comments = pd.read_excel("./raw.xlsx", header=None)

stage1 = pd.DataFrame(columns=comments.columns)
stage2 = pd.DataFrame(columns=comments.columns) 
stage3 = pd.DataFrame(columns=comments.columns) 


# Stage1: Remove the rows of comments which are blank and beyond the required date range
# Remove the blank comments
lineOfStage1 = 0
for i in range(0, len(comments)):
    if str(comments.iloc[i,1]) == 'nan' or str(comments.iloc[i,1]) == 'Nan': # Determine whether the second column of this file is blank
        continue # If it is, then skip

    commentTimeStamp = comments.iloc[i, 2][:6]  # Locate the third column in row i of this file, select the first six characters in string
    if commentTimeStamp[1:2] != '2' and  commentTimeStamp[1:2] != '3':
        continue # If the month is not February or March, then skip this row and determine next row
    #Case1: The month is February
    if commentTimeStamp[1:2] == '2': 
        day = int(commentTimeStamp[3:5])
        if day < 24:
            continue # If the date is smaller than 24, then skip this row and determine next row
        else:
            stage1.loc[lineOfStage1] = comments.iloc[i,:] # After filtering, add the rows whose date is between February 24th and February 28th to the Stage1 DataFrame
            lineOfStage1 += 1
    #Case2: The month is March
    if commentTimeStamp[1:2] == '3': 
        day = int(commentTimeStamp[3:5])
        if day > 2:
            continue # If the date is bigger than 2, then skip this row and determine next row
        else:
            stage1.loc[lineOfStage1] = comments.iloc[i,:] # After filtering, add the rows whose date is between March 1st and March 2nd to the Stage1 DataFrame
            lineOfStage1 += 1 

# print(stage1)

# Stage2: Numeric values processing - remove "?" 
lineOfStage2 = 0
for i in range(0, len(stage1)):
    # print(stage1.iloc[i, 2][12:13])  "?" in the third column is the 13th character
    stage2.loc[lineOfStage2] = stage1.loc[i] # Copy the rows of stage1 to stage2
    # Combine the 1st to 12th characters and the characters after the 13th (the 13th character is skipped, which means "?" is skipped)
    stage2.iloc[lineOfStage2, 2] = stage2.iloc[lineOfStage2, 2][:12] + stage2.iloc[lineOfStage2, 2][13:] 
    assert(lineOfStage2 == i)
    lineOfStage2 += 1 

# print(stage2)

# Stage3: Text processing - remove "the reply @xxx:" 
for i in range(0, len(stage2)):
    print(stage2.iloc[i, 1])
    # There may be multiple "回复@users_name:", so we use a loop to determine if the first three words of the comment are "回复@"
    # If not, jump directly to the end to copy this row to stage3
    while str(stage2.iloc[i, 1])[:3] == "回复@":  
        for j in range(3, len(str(stage2.iloc[i,1]))): # Running this line means the first three words must be "回复@" 
                                                       # Next, we have to find ":". Use variable j to traverse from the third word until [j] is ":"
            if stage2.iloc[i, 1][j] != ':': 
                continue 
            else: # [j] is ":"
                stage2.iloc[i,1] = stage2.iloc[i,1][j + 1:] # Remove all characters before the j, leave the j + 1th character and the part after it (the part after ":")
                break
    stage3.loc[i] = stage2.loc[i]

print(stage3)

stage3.to_excel("./result.xlsx", index = False)