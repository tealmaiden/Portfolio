# Combine Raw Data from DNA Tests
6-19-2021

## Background
Commercial genetic testing services like 23andme and Ancestry.com don't conduct their analyses by sequencing your entire genome. At the time of this writing, this isn't technologically feasible yet.
Instead, these services search for a large number of known sequences called single nucleotide polymorphisms (SNPs), which are associated with a genotype (AA, GG, AG, CT, CC, etc.).
Different testing services have different sets of SNPs they check for, which may overlap. Your genotype for each SNP tested is recorded in a raw downloadable data file. 

InsideTracker (an external analysis service) allows you to upload your raw data results, but only lets you upload one file. I have test results from both 23andme and Ancestry and wanted to consolidate them for this purpose. This would give me a larger data set to be analyzed.

## Objective
Combine raw SNP data without duplicates into a single text file. 

## Steps Taken
1. Removed introductory paragraphs from both text files.
2. Chose Python because I am relatively familiar with its file scripting tools.
3. Opened the text files in Python.
4. Using the csv python package, read the files with dialect="excel-tab" because the values in each text file rows are separated by tabs.
5. Cast the file data into lists (datasets).
6. Tracked duplicate SNPs in a frequency table and counting variable.
7. If the SNP from a line from second file's dataset was not a duplicate, reformatted the line to match that of the first dataset and appended that line to the first dataset.
8. Joined the consolidated dataset lines with tabs and wrote the results to a new text file separated by newlines.

## Results
A consolidated text file of data was produced which was larger than both parent files (23andme had 963049 lines of data, Ancestry had 677864, and combined  result had 1173037). There were 467876 duplicates recorded, which is consistent with the result file size.

The file was successfully submitted to InsideTracker, however their gene analysis doesn't appear to be that detailed or useful, so just submitting either original file probably would have not made a difference in this case.
