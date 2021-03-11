import datetime


def create_employment_letter(ans):
    if ans['mood'] == 'A':
        letter = create_annoyed_letter(ans)
        return letter
    elif ans['mood'] == 'B':
        letter = create_calm_letter(ans)
        return letter
    else:
        letter = create_angry_letter(ans)
        return letter


def create_annoyed_letter(ans):
    date = datetime.date.today()
    date = date.strftime("%m/%d/%Y")
    u = datetime.datetime.strptime(date, "%m/%d/%Y")
    d = datetime.timedelta(days=21)
    letter = f"""
{ans['name']}<br>
{ans['address']}<br><br>

{date}<br><br>

{ans['boss_name']}<br>
{ans['company_address']}<br><br>

Re: Formal Response to Termination Without Cause<br><br>

Dear {ans['company_name']} Superior,<br><br>

I appreciated my time spent at {ans['company_name']}. While I respect that fact that my layoff was not personal, 
I do feel that I am not being treated fairly and have not been offered the compensation that I am entitled to under 
the circumstances.<br><br>

When I joined the company {ans['time_worked']['years']} years and {ans['time_worked']['months']} months ago as a {ans['job_title']}, 
I looked forward to being an impactful team member. Since {ans['job_start_date']}, 
I was a reliable and diligent employee at {ans['company_name']}. I truly embodied ou r company’s 
inclusive and professional culture. With {ans['experience']} years of experience in my field, 
I brought a wealth of knowledge and skill to {ans['company_name']}. My layoff was an abrupt 
shock to an otherwise excellent working relationship.<br><br>

[A]Thank you for the offer of {ans['severance']} weeks of severance. Unfortunately, 
it falls well below what I am entitled to under prevailing employment legislation. 
Most notably, it will be difficult for me to find suitable work to match my experience and skills. 
I am therefore entitled to additional compensation.<br><br>

Given the circumstances, and in the interest of putting this behind us, I would be willing to accept
[ALL OPTIONS HERE]<br><br>

Please respond within X (days/weeks) to indicate your acceptance of the offer. Otherwise, 
I may be forced to pursue more formal legal action.<br><br>

Sincerely,<br><br>

{ans['name']}
"""
    return letter



def create_calm_letter(ans):
    date = datetime.date.today()
    date = date.strftime("%m/%d/%Y")

    u = datetime.datetime.strptime(date, "%m/%d/%Y")
    d = datetime.timedelta(days=21)
    response_date = u + d
    response_date = response_date.strftime("%m/%d/%Y")
    return f"""<pre>{date}

{ans['name']}

{ans['address']}

{ans['boss_name']}
{ans['company_address']}

Re: Response to Layoff

Dear {ans['company_name']} Superior,

I appreciated my time spent at {ans['company_name']} . While I respect that fact that my layoff was not personal, I do feel that I am not being treated fairly and have not been offered the compensation that I am entitled to under the circumstances.

When I joined the company {ans['time_worked']} ago as a ???XYZ Title???, I looked forward to being an impactful team member. Since ???XYZ Date???, I was a reliable and diligent employee at {ans['company_name']} . I truly embodied our company’s inclusive and professional culture.
 
 With {ans['time_worked']} of experience in my field, I brought a wealth of knowledge and skill to {ans['company_name']} .

There was nothing to indicate, leading up to my dismissal, that there were any issues with my performance. My layoff was an abrupt shock to an otherwise excellent working relationship.

Thank you for the offer of {ans['severance']} of severance. it falls well below what I am entitled to under the “reasonable notice” requirement at common law. Most notably, it will be difficult for me to find suitable work to match my experience and skills. I am therefore entitled to additional compensation.

Given the circumstances, and in the interest of putting this behind us, I would be willing to accept {ans['severance']} of pay plus all unpaid/unused vacation time that is accrued up until that point as severance, which is ???Y days/$$$???. This offer is fair and reasonable to both of us.

Please respond by {ans['name']} and indicate your acceptance of this offer. Otherwise, I may be forced to pursue more formal legal action.

Sincerely, {ans['name']} </pre>"""


def create_angry_letter(ans):
    return f"""<pre>DATE

NAME OF EMPLOYEE

ADDRESS

NAME OF EMPLOYER
ADDRESS

Re: Layoff

I'm incredibly shocked and disappointed to have been laid off from XYZ 

When I joined the company in XXX, I was led to believe the Canadian team was being built for growth, and that I would be building a creative team in Vancouver within a year. This did not happen. No team was built; nor did I feel any active attempt was made to do so. I feel grossly misled. Not having any team and being the sole creative in the office is a dark spot on my resume.

I left a secure and stable job at YYY where I had ZZZ years tenure and a large and supportive team, to work for XXX. I was told there was ample funding and backing for the Canadian business, creating a stable work environment. Again, I feel misled. 

I was notified of my dismissal by proxy. The process was immediate and jarring. Mr A, Mr B, this gave me no opportunity to ask questions or get clarity. 

The layoff is not only causing me distress but is also doing harm to my reputation and career. At my level, a new opportunity can take up to a year to source. 

Your 3 weeks severance offer is unacceptable. I am aware of my contractual rights, which purport to limit my right to severance. However, I believe I am entitled to a more significant severance for the following reasons: 

I feel misled and that you misrepresented XXX’s intention for my role and its Canadian operations 
My very abbreviated tenure will damage my reputation and make it more difficult to find suitable work at my level
The way I was laid off was improper - it did not provide an opportunity for explanation; and especially so since you were in the office the previous week but neglected to notify me - a very senior position - in person. 

For these reasons, I will accept an offer of YYY weeks of severance pay. This offer is open for you to accept until this ZZZ,  after which point I may be forced to take further action. 

Despite the shortcomings, I've really enjoyed the last YYY months and getting to know the XXX family. I was truly excited to build something great  - and I have gotten the sense that XXX cares about its employees. Please don't make me feel misled again. 

Thank you. </pre>"""
