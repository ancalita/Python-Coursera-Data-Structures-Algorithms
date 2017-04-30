Multiple Pattern Matching
Problem Introduction
Given a string Text and Trie(Patterns), we can quickly check whether any string from Patterns matches a prefix of Text.
To do so, we start reading symbols from the beginning of Text and see what string these symbols “spell” as we proceed along the path downward from the root of the trie.
For each new symbol in Text, if we encounter this symbol along an edge leading down from the present node, then we continue along this edge; otherwise, we stop and conclude that no string in Patterns matches a prefix of Text.
If we make it all the way to a leaf, then the pattern spelled out by this path matches a prefix of Text.
This algorithm is called PrefixTrieMatching.
PrefixTrieMatching finds whether any strings in Patterns match a prefix of Text.
To find whether any strings in Patterns match a substring of Text starting at position 𝑘, we chop off the first 𝑘 − 1 symbols from Text and run PrefixTrieMatching on the shortened string.
As a result, to solve the Multiple Pattern Matching Problem, we simply iterate PrefixTrieMatching |Text| times, chopping the first symbol off of Text before each new iteration.
Note that in practice there is no need to actually chop the first 𝑘 − 1 symbols of Text.
Instead, we just read Text from the 𝑘-th symbol.
Input Format. The first line of the input contains a string Text,each of the following 𝑛 lines contains a pattern from Patterns = {𝑝1 , . . . , 𝑝𝑛 }.
Constraints. 1≤|Text|≤10000;1≤𝑛≤5000;1≤|𝑝𝑖|≤100 for all 1≤𝑖≤𝑛;all strings contain only symbols A,C,G,T;no 𝑝𝑖 is a prefix of 𝑝𝑗 for all 1≤𝑖̸=𝑗≤𝑛.
Output Format. All starting positions in Text where a string from Patterns appears as a substring in
increasing order (assuming that Text is a 0-based array of symbols).
