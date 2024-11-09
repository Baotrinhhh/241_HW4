"""
UMass ECE 241 - Advanced Programming
Homework #4     Fall 2023
question2.py - AVL Trees
"""


class Question2:
    @staticmethod
    def balancedTrees():
        """
        Return the list of trees that are balanced.
        
        Choose all that applies from "a", "b", "c", and "d"
        
        For example, if you think a, c are balanced and b, d
        are unbalanced, you should return ["a", "c"]
        """
        
        return []
    
    @staticmethod
    def balanceFactors():
        """
        Return the balance factor of each tree (at root).
        When calculating the balance factor, using left height - right height.
        """
        
        return {
            "a": 0,     # balance factor for root node for tree (a)
            "b": 0,     # balance factor for root node for tree (b)
            "c": 0,     # balance factor for root node for tree (c)
            "d": 0      # balance factor for root node for tree (d)
        }
        
    @staticmethod
    def insertion():
        """
        Fill in the AVL tree list after inserting
        10, 20, 15, 25, 30, 16, 18, 19
        according to the question.
        First two steps is done for you. 
        """
        AVL_tree_lists = [
            [10],
            [10, None, 20],
            
        ]
        
        """
        Fill in the balance factor lists 
        for each steps of the AVL_tree_lists above.
        First two steps is done for you.
        """
        balance_factors = [
            [0],
            [-1, None, 0],
            
        ]
        
        return {
            "AVL_tree_lists": AVL_tree_lists,
            "balance_factors": balance_factors
        }


if __name__ == "__main__":
    pass