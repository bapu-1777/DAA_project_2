# CSE 5311 - PROJECT 2

Vekariya, Mayank - 1002078999

Shukla, Tirth - 1002050571

CSE5311-08-P2-1002078999-1002050571


An example of a subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements in the sequence.

In order to find the longest common subsequence (LCS) between two sequences, we have to find a subsequence with a maximum length, that is common to both sequences. As an example, if two strings "ace" and "abcde" are given, the longest common subsequence is 3, which is "ace".


## logic

As an example, let's find the longest common subsequence between the strings "abc" and "cab".

Approach: Start filling each row of the dpTable and fill all the columns in one row before moving to the next row. This solves sub-problems that help arrive at the results of the actual problem.

The longest common subsequence is 0, because if either of the two strings is empty, they may have nothing in common. So in the dpTable all the values ​​in the first row and first column are 0.

When filling a cell dpTable[i][j] there are two cases

str1[i] == str2[j] where dpTable[i][j] = dpTable[i - 1] [ j - 1] + 1
str1[i] != str2[j], where dpTable[i][j] = Math.max(dpTable[i - 1][j], dpTable[i][j - 1]))

## Deployment

To deploy this project or To run this project

```bash
1. extract(open) this zip file
2. open the project folder in pycharm/vs_code_editer and check the dependency
3. at last, run all three ".py" files.
```

## project structure

files and folders structure

````bash
.
├── code.py
├── project_report.pdf
└── README.md

````

## Reference For Development

 - [programiz - To Learn File Opretion in python](https://www.programiz.com/python-programming)
 - [Codebasics - Some YouTube Videos](https://www.youtube.com/watch?v=_t2GVaQasRY&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12)
 
## Documentation

[Project Report](https://linktodocumentation)


## Optimizations

we can do more optimization and understand using adding an extra ".py" file for a major operation.

## Feedback

If you have any feedback, please reach out to us at mxv8999@mavs.uta.edu


## Lessons Learned

in this project we learned sorting algorithms (merge, quick, insertion) and time complexity.

## Authors

- [@mayankvekariya](https://www.linkedin.com/in/mayank-vekariya-468214180/)
- [@shukla](https://www.linkedin.com/in/tirth-shukla/)

## License

[UTA](https://www.uta.edu/)


