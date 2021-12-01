from werkzeug.datastructures import ImmutableMultiDict

class CellphoneGenerator:
    def __init__(self, ans):
        self.ans = ans.to_dict(flat=False)
        print(self.ans)
    
    # def to_dict(self):
    #     for i in self.ans:
    #         print(f"index0: {i[0]} index1: {i[1]}")
