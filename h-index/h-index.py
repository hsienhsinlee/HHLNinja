#!/usr/local/bin/python3

citation_count = [8, 4, 5, 2, 45, 20, 11, 5, 5, 6, 7, 7, 12, 3, 13, 14, 5, 6 , 9, 10]

participants = {
    1 : {
        "name": "Alan Turing",
        "citation": [12, 45, 23, 12, 23, 2, 31, 4, 5, 1, 1, 31],
        "sorted_citation": [],
        "h-index": 0
    },
    2 : {
        "name": "Edward McCluskey",
        "citation": [8, 4, 5, 2, 45, 20, 11, 5, 5, 6, 7, 7, 12, 3, 13, 14, 5, 6 , 9, 10],
        "sorted_citation": [],
        "h-index": 0
    },
    3 : {
        "name": "Albert Einstein",
        "citation": [121, 213, 12, 123, 122, 64, 13, 12, 3, 5, 61, 23, 122, 9, 7, 10, 23],
        "sorted_citation": [],
        "h-index": 0
    },
    4 : {
        "name": "Mark Zuck",
        "citation": [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1],
        "sorted_citation": [],
        "h-index": 0
    },
    5 : {
        "name": "James E. Smith",
        "citation": [2, 4, 4, 3, 5, 6, 7, 6, 8, 4, 3, 2, 6, 7, 5, 9],
        "sorted_citation": [],
        "h-index": 0
    },
    6 : {
        "name": "Klaus-RObert Muller",
        "citation": [12, 41, 14, 33, 25, 16, 71, 8, 8, 1, 1, 1, 1, 1, 2, 9],
        "sorted_citation": [],
        "h-index": 0
    },
    6 : {
        "name": "Alex K. Jones",
        "citation": [1, 1, 1, 1, 2, 1, 1, 2],
        "sorted_citation": [],
        "h-index": 0
    },
}

for p in participants:

    sorted_citation_count = sorted(participants[p]["citation"], reverse=True)  # sorted list in the original list
    participants[p]["sorted_citation"] = sorted_citation_count.copy()

    h_index = 0
    for i in sorted_citation_count:
        if (i > h_index):
            h_index += 1
        else:
            break
    participants[p]["h-index"] = h_index

# print the new list with H-Index
for p in participants:
    print(participants[p]["name"],"H-Index=", participants[p]["h-index"],
                        ", Sorted citation =", participants[p]["sorted_citation"])
