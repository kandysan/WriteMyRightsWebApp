from werkzeug.datastructures import ImmutableMultiDict

class CellphoneGenerator:
    def __init__(self, ans):
        self.ans = ans.to_dict(flat=False)
        print(self.ans)
        self.letter_content = ""
        self.generate_letter()

    def generate_letter(self):
        self.letter_content = f"""
{self.ans['question' + '1'][0]}
{self.ans['question' + '2'][0]}
EMAIL ADDRESS 

{self.ans['question' + '0'][0]}

{self.ans['question' + '3'][0]}
{self.ans['question' + '4'][0]}

Dear {self.ans['question' + '3'][0]},

Re: Complaint about cell phone charges
I’m complaining because I have been overcharged. I’ve attempted to resolve this matter through your customer service department but have either been left on hold for an unreasonable amount of time, or haven’t gotten the response I’ve been looking for. 
You’ve overcharged me for ${self.ans['question' + '6'][0]}. I believe I am entitled to a refund of ${self.ans['question' + '6'][0]}. {f"[SEE NUMBER 9 ONLY IF THEY SAY YES] When I learned of this problem, I contacted {self.ans['question' + '9'][0]} at your company on [date of the contact]." if self.ans['question' + '8'][0] == "Yes" else ""} {f" I was promised a refund in the amount of ${self.ans['question' + '13'][0]} which I still have not received" if self.ans['question' + '11'][0] == 'Yes' else ''}

Hopefully this written letter can get this resolved. I’ve been a loyal customer {"for over three years " if self.ans['question' + '1'][0] == "More than three years" else ""}and want to keep giving {self.ans['question' + '3'][0]} my business. {"I’ll highlight here that I’m on a month to month contract." if self.ans['question' + '12'][0] == 'Month-to-Month' else ''} I can take my business to any cell phone provider I want. I’d rather not have to do that though, so hopefully you can make this right.


I look forward to your reply and to resolving the problem, and will wait {self.ans['question' + '13'][0]} before taking my next step[QUESTION 12 based on answer]{", which may include a complaint to the local ombudsperson, filing a claim in small claims court, or voicing my concerns over social media or through local news outlets" if True else "."}. I’d rather not let it come to that, though.
Please contact me by email at {self.ans['question' + '16'][0]}{" or by telephone at " + str(self.ans['question' + '17'][0]) if self.ans['question' + '17'][0] != "" else ""}.
Sincerely,
{self.ans['question' + '1'][0]}
        """
        print(self.letter_content)
    # def to_dict(self):
    #     for i in self.ans:
    #         print(f"index0: {i[0]} index1: {i[1]}")
