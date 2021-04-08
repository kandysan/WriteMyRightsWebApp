#letter template scripts

PAYMENT = True

def create_employment_letter(ans):
    ''' letter choice based on mood '''
    if ans['mood'] == 'a' or ans['mood'] == 'A':
        letter = create_annoyed_letter(ans)
    elif ans['mood'] == 'b' or ans['mood'] == 'B':
        letter = create_angry_letter(ans)
    else:
        letter = create_sad_letter(ans)
    return letter


def create_employment_letter_preview(ans):
    ''' letter preview based on mood '''
    if ans['mood'] == 'a' or ans['mood'] == 'A':
        letter_preview = create_annoyed_letter_preview(ans)
    elif ans['mood'] == 'b' or ans['mood'] == 'B':
        letter_preview = create_angry_letter_preview(ans)
    else:
        letter_preview = create_sad_letter_preview(ans)
    return letter_preview


def create_annoyed_letter(ans):
    ''' template of annoyed letter for word doc '''
    letter = f"""{ans['name']}
{ans['personal_address']}

{ans['date']}

{ans['boss_name']}
{ans['company_address']}

Re: Response to Layoff

Dear {ans['company_name']} Superior,

I appreciated my time spent at {ans['company_name']}. While I respect that fact that my layoff was not personal, I do feel that I am not being treated fairly and have not been offered the compensation that I am entitled to under the circumstances. """
    if PAYMENT == True:
        letter += f"""
        
When I joined the company"""
        if ans['months_worked'] != 0 and ans['years_worked'] != 0:
            if ans['years_worked'] != 1:
                letter += f""" {ans['years_worked']} years """
            else:
                letter += ' 1 year '
            if ans['months_worked'] != 1:
                letter += f"""and {ans['months_worked']} months """
            else:
                letter += 'and 1 month '
        else:
            if ans['months_worked'] != 0:
                if ans['months_worked'] != 1:
                    letter += f""" {ans['months_worked']} months """
                else:
                    letter += ' 1 month '
            else:
                if ans['years_worked'] != 1:
                    letter += f""" {ans['years_worked']} years """
                else:
                    letter += ' 1 year '
        letter += f"""ago as a {ans['job_title']}, I looked forward to being an impactful team member. Since {ans['job_start_date']}, I was a reliable and diligent employee at {ans['company_name']}. I truly embodied our company’s inclusive and professional culture. With {ans['experience']} years of experience in my field, I brought a wealth of knowledge and skill to {ans['company_name']}. My layoff was an abrupt shock to an otherwise excellent working relationship. """
    else:
        pass
    
    letter += f"""

Thank you for the offer of {ans['severance_paid']} weeks of severance. Unfortunately, it falls well below what I am entitled to under prevailing employment legislation. Most notably, it will be difficult for me to find suitable work to match my experience and skills. I am therefore entitled to additional compensation. 

Given the circumstances, and in the interest of putting this behind us, I would be willing to accept"""

    if ans['severance_demand'] != '0' and ans['vacation'] != '0' and ans['apology'] == 'yes':
        #B, C and D
        letter += f""" {ans['severance_demand']} weeks of pay plus all unpaid vacation time that has accrued up until my termination which is {ans['vacation']} weeks. I also want a written apology for all of the hardship that I suffered. """
    elif ans['severance_demand'] != '0' and ans['vacation'] != '0':
        # B and C
        letter += f""" {ans['severance_demand']} weeks of pay plus all unpaid vacation time that has accrued up until my termination which is {ans['vacation']} weeks."""
    elif ans['severance_demand'] != '0':
        # B
        letter += f""" {ans['severance_demand']} weeks of pay. This offer is fair and reasonable to both of us."""
    elif ans['apology'] == 'yes':
        letter += f"""a written apology for all of the hardship that I suffered."""

    letter += f"""
    
Please respond by {ans['response_date']} to indicate your acceptance of the offer. Otherwise, I may be forced to pursue more formal legal action.

Sincerely,

{ans['name']}"""
    return letter


def create_angry_letter(ans):
    ''' template of angry letter for word doc '''
    letter = f"""{ans['name']}
{ans['personal_address']}

{ans['date']}

{ans['boss_name']}
{ans['company_address']}

Re: Formal Response to Termination Without Cause

Dear {ans['company_name']} Superior,

I’m shocked and disappointed to be laid off by {ans['company_name']}. I have been a key member of the {ans['job_title']} team for"""
    if ans['months_worked'] != 0 and ans['years_worked'] != 0:
        if ans['years_worked'] != 1:
            letter += f""" {ans['years_worked']} years """
        else:
            letter += ' 1 year '
        if ans['months_worked'] != 1:
            letter += f"""and {ans['months_worked']} months """
        else:
            letter += 'and 1 month '
    else:
        if ans['months_worked'] != 0:
            if ans['months_worked'] != 1:
                letter += f""" {ans['months_worked']} months """
            else:
                letter += ' 1 month '
        else:
            if ans['years_worked'] != 1:
                letter += f""" {ans['years_worked']} years """
            else:
                letter += ' 1 year '
    letter += f"""now."""

    if PAYMENT == True:
        letter += f"""
        
The company’s vision aligns with my values and aspirations, and I anticipated a long and fruitful relationship with {ans['company_name']}. I have been a committed and dedicated employee since day 1 - being let go like this is unjustified and wrong. My layoff was an abrupt shock to an otherwise excellent working relationship - it is not only causing me distress but is also doing harm to my reputation and career. At my level, a new opportunity can take {ans['findJobLength']} to source."""
    else:
        pass

    letter += f"""
    
Your offer of {ans['severance_paid']} weeks of severance is less than what I believe I am entitled to. Given the situation, the industry, and the position I held, I believe I am entitled to a minimum of {ans['severance_demand']} weeks of severance."""

    if PAYMENT == True:
        letter += f"""
        
At this point, I would like to be able to come to an agreement without resorting to more formal options. I highly respect {ans['company_name']} and what it is trying to accomplish. But given a number of factors mentioned above (including my level of seniority, reputation, and career prospects), I need to look out for my interests given the situation."""
    else:
        pass

    letter += f"""
    
Given the circumstances, and in the interest of putting this behind us, I would be willing to accept"""

    if ans['severance_demand'] != 'none' and ans['vacation'] != 'none':
        #B, C and D
        letter += f""" {ans['severance_demand']} weeks of pay plus all unpaid vacation time that has accrued up until my termination which is {ans['vacation']} weeks. I also want a written apology for all of the hardship that I suffered. """
    elif ans['severance_demand'] != 'none' and ans['vacation'] != 'none':
        # B and C
        letter += f""" {ans['severance_demand']} weeks of pay plus all unpaid vacation time that has accrued up until my termination which is {ans['vacation']} weeks."""
    elif ans['severance_demand'] != 'none':
        # B
        letter += f""" {ans['severance_demand']} weeks of pay. This offer is fair and reasonable to both of us."""
    elif ans['apology'] == 'yes':
        letter += f"""a written apology for all of the hardship that I suffered."""

    letter += f""" Please respond by {ans['response_date']} to indicate your acceptance of the offer. Otherwise, I may be forced to pursue further legal action.

Sincerely,

{ans['name']}"""
    return letter



def create_sad_letter(ans):
    ''' template of sad letter for word doc '''
    letter = f"""{ans['name']}
{ans['personal_address']}

{ans['date']}

{ans['boss_name']}
{ans['company_address']}

Re: Layoff

When I joined"""
    if ans['months_worked'] != 0 and ans['years_worked'] != 0:
        if ans['years_worked'] != 1:
            letter += f""" {ans['years_worked']} years """
        else:
            letter += ' 1 year '
        if ans['months_worked'] != 1:
            letter += f"""and {ans['months_worked']} months """
        else:
            letter += 'and 1 month '
    else:
        if ans['months_worked'] != 0:
            if ans['months_worked'] != 1:
                letter += f""" {ans['months_worked']} months """
            else:
                letter += ' 1 month '
        else:
            if ans['years_worked'] != 1:
                letter += f""" {ans['years_worked']} years """
            else:
                letter += ' 1 year '
    letter += f"""ago, it was an exciting time. I was truly looking forward to helping our team to succeed. But now, I'm incredibly shocked and disappointed to have been laid off."""

    if PAYMENT == True:
        letter += f"""
        
The company’s vision aligns so well with my values. I have been a committed and dedicated employee since day 1 - being let go like this just feels wrong. It’s an abrupt shock to an otherwise excellent working relationship. It’s caused me distress, and may seriously harm my reputation and career. At my level, a new opportunity can take {ans['findJobLength']} to find."""
    else:
        pass

    letter += f"""
    
Thank you for the {ans['severance_paid']} weeks of severance offered. Unfortunately, I can’t accept it. I believe I am legally entitled to a bigger severance payment, owing to the abruptness of the layoff and the potential damage to my reputation, and career prospects. Under the circumstances, and in the interest of putting this behind us, I would be willing to accept"""

    if ans['severance_demand'] != 'none' and ans['vacation'] != 'none' and ans['apology'] == 'yes':
        #B, C and D
        letter += f""" {ans['severance_demand']} weeks of pay plus all unpaid vacation time that has accrued up until my termination which is {ans['vacation']} weeks. I also want a written apology for all of the hardship that I suffered. """
    elif ans['severance_demand'] != 'none' and ans['vacation'] != 'none':
        # B and C
        letter += f""" {ans['severance_demand']} weeks of pay plus all unpaid vacation time that has accrued up until my termination which is {ans['vacation']} weeks."""
    elif ans['severance_demand'] != 'none':
        # B
        letter += f""" {ans['severance_demand']} weeks of pay. This offer is fair and reasonable to both of us."""
    elif ans['apology'] == 'yes':
        letter += f"""a written apology for all of the hardship that I suffered."""

    if PAYMENT == True:
        letter += f"""
        
Despite the shortcomings, I've really enjoyed the last"""
        if ans['months_worked'] != 0 and ans['years_worked'] != 0:
            if ans['years_worked'] != 1:
                letter += f""" {ans['years_worked']} years """
            else:
                letter += ' 1 year '
            if ans['months_worked'] != 1:
                letter += f"""and {ans['months_worked']} months """
            else:
                letter += 'and 1 month '
        else:
            if ans['months_worked'] != 0:
                if ans['months_worked'] != 1:
                    letter += f""" {ans['months_worked']} months """
                else:
                    letter += ' 1 month '
            else:
                if ans['years_worked'] != 1:
                    letter += f""" {ans['years_worked']} years """
                else:
                    letter += ' 1 year '
        letter += f"""and getting to know the {ans['company_name']} family. I was truly excited to build something great  - and I have gotten the sense that {ans['company_name']} cares about its employees. Please don't make me feel misled."""
    else:
        pass

    letter += f"""
    
Please let me know your intentions by {ans['response_date']}.

Thank you,

{ans['name']}"""

    return letter


def create_annoyed_letter_preview(ans):
    letter = f"""{ans['name']}<br>
{ans['personal_address']}
<br><br>
{ans['date']}
<br><br>
{ans['boss_name']}<br>
{ans['company_address']}
<br><br>
Re: Response to Layoff
<br><br>
Dear {ans['company_name']} Superior,
<br><br>
I appreciated my time spent at {ans['company_name']}. While I respect that fact that my layoff was not personal, I do feel that I am not being treated fairly and have not been offered the compensation that I am entitled to under the circumstances.
<br><br>
<p class="blurText">When I joined the company"""
    if ans['months_worked'] != 0 and ans['years_worked'] != 0:
        if ans['years_worked'] != 1:
            letter += f""" {ans['years_worked']} years """
        else:
            letter += ' 1 year '
        if ans['months_worked'] != 1:
            letter += f"""and {ans['months_worked']} months """
        else:
            letter += 'and 1 month '
    else:
        if ans['months_worked'] != 0:
            if ans['months_worked'] != 1:
                letter += f""" {ans['months_worked']} months """
            else:
                letter += ' 1 month '
        else:
            if ans['years_worked'] != 1:
                letter += f""" {ans['years_worked']} years """
            else:
                letter += ' 1 year '
    letter += f"""ago as a {ans['job_title']}, I looked forward to being an impactful team member. Since {ans['job_start_date']}, I was a reliable and diligent employee at {ans['company_name']}. I truly embodied our company’s inclusive and professional culture. With {ans['experience']} years of experience in my field, I brought a wealth of knowledge and skill to {ans['company_name']}. My layoff was an abrupt shock to an otherwise excellent working relationship.</p>
<br><br>
Thank you for the offer of {ans['severance_paid']} weeks of severance. Unfortunately, it falls well below what I am entitled to under prevailing employment legislation. Most notably, it will be difficult for me to find suitable work to match my experience and skills. I am therefore entitled to additional compensation. 
<br><br>
Given the circumstances, and in the interest of putting this behind us, I would be willing to accept"""

    if ans['severance_demand'] != '0' and ans['vacation'] != '0' and ans['apology'] == 'yes':
        # B, C and D
        letter += f""" {ans['severance_demand']} weeks of pay plus all unpaid vacation time that has accrued up until my termination which is {ans['vacation']} weeks. I also want a written apology for all of the hardship that I suffered. """
    elif ans['severance_demand'] != '0' and ans['vacation'] != '0':
        # B and C
        letter += f""" {ans['severance_demand']} weeks of pay plus all unpaid vacation time that has accrued up until my termination which is {ans['vacation']} weeks."""
    elif ans['severance_demand'] != '0':
        # B
        letter += f""" {ans['severance_demand']} weeks of pay. This offer is fair and reasonable to both of us."""
    elif ans['apology'] == 'yes':
        letter += f"""a written apology for all of the hardship that I suffered."""

    letter += f"""<br><br>Please respond by {ans['response_date']} to indicate your acceptance of the offer. Otherwise, I may be forced to pursue more formal legal action.
<br><br>
Sincerely,
<br><br>
{ans['name']}"""
    return letter


def create_angry_letter_preview(ans):
    ''' template of annoyed letter preview (unpaid) for word doc '''
    letter = f"""{ans['name']}<br>
    {ans['personal_address']}
<br><br>
    {ans['date']}
<br><br>
    {ans['boss_name']}<br>
    {ans['company_address']}
<br><br>
    Re: Formal Response to Termination Without Cause
<br><br>
    Dear {ans['company_name']} Superior,
<br><br>
    I’m shocked and disappointed to be laid off by {ans['company_name']}. I have been a key member of the {ans['job_title']} team for"""
    if ans['months_worked'] != 0 and ans['years_worked'] != 0:
        if ans['years_worked'] != 1:
            letter += f""" {ans['years_worked']} years """
        else:
            letter += ' 1 year '
        if ans['months_worked'] != 1:
            letter += f"""and {ans['months_worked']} months """
        else:
            letter += 'and 1 month '
    else:
        if ans['months_worked'] != 0:
            if ans['months_worked'] != 1:
                letter += f""" {ans['months_worked']} months """
            else:
                letter += ' 1 month '
        else:
            if ans['years_worked'] != 1:
                letter += f""" {ans['years_worked']} years """
            else:
                letter += ' 1 year '
    letter += f"""now.
<br>
    <p class="blurText">The company’s vision aligns with my values and aspirations, and I anticipated a long and fruitful relationship with {ans['company_name']}. I have been a committed and dedicated employee since day 1 - being let go like this is unjustified and wrong. My layoff was an abrupt shock to an otherwise excellent working relationship - it is not only causing me distress but is also doing harm to my reputation and career. At my level, a new opportunity can take {ans['findJobLength']} to source.</p>

    Your offer of {ans['severance_paid']} weeks of severance is less than what I believe I am entitled to. Given the situation, the industry, and the position I held, I believe I am entitled to a minimum of {ans['severance_demand']} weeks of severance.

    <p class="blurText">At this point, I would like to be able to come to an agreement without resorting to more formal options. I highly respect {ans['company_name']} and what it is trying to accomplish. But given a number of factors mentioned above (including my level of seniority, reputation, and career prospects), I need to look out for my interests given the situation.</p>

    Given the circumstances, and in the interest of putting this behind us, I would be willing to accept"""

    if ans['severance_demand'] != 'none' and ans['vacation'] != 'none' and ans['apology'] == 'yes':
        # B, C and D
        letter += f""" {ans['severance_demand']} weeks of pay plus all unpaid vacation time that has accrued up until my termination which is {ans['vacation']} weeks. I also want a written apology for all of the hardship that I suffered. """
    elif ans['severance_demand'] != 'none' and ans['vacation'] != 'none':
        # B and C
        letter += f""" {ans['severance_demand']} weeks of pay plus all unpaid vacation time that has accrued up until my termination which is {ans['vacation']} weeks."""
    elif ans['severance_demand'] != 'none':
        # B
        letter += f""" {ans['severance_demand']} weeks of pay. This offer is fair and reasonable to both of us."""
    elif ans['apology'] == 'yes':
        letter += f"""a written apology for all of the hardship that I suffered."""

    letter += f"""<br><br>Please respond by {ans['response_date']} to indicate your acceptance of the offer. Otherwise, I may be forced to pursue further legal action.
<br><br>
    Sincerely,
<br><br>
    {ans['name']}"""
    return letter


def create_sad_letter_preview(ans):
    ''' template of sad letter preview (unpaid) for word doc '''
    letter = f"""{ans['name']}<br>
    {ans['personal_address']}
<br><br>
    {ans['date']}
<br><br>
    {ans['boss_name']}<br>
    {ans['company_address']}
<br><br>
    Re: Layoff
<br><br>
    When I joined"""
    if ans['months_worked'] != 0 and ans['years_worked'] != 0:
        if ans['years_worked'] != 1:
            letter += f""" {ans['years_worked']} years """
        else:
            letter += ' 1 year '
        if ans['months_worked'] != 1:
            letter += f"""and {ans['months_worked']} months """
        else:
            letter += 'and 1 month '
    else:
        if ans['months_worked'] != 0:
            if ans['months_worked'] != 1:
                letter += f""" {ans['months_worked']} months """
            else:
                letter += ' 1 month '
        else:
            if ans['years_worked'] != 1:
                letter += f""" {ans['years_worked']} years """
            else:
                letter += ' 1 year '
    letter += f"""ago, it was an exciting time. I was truly looking forward to helping our team to succeed. But now, I'm incredibly shocked and disappointed to have been laid off.

    <p class="blurText">The company’s vision aligns so well with my values. I have been a committed and dedicated employee since day 1 - being let go like this just feels wrong. It’s an abrupt shock to an otherwise excellent working relationship. It’s caused me distress, and may seriously harm my reputation and career. At my level, a new opportunity can take {ans['findJobLength']} to find.</p>

    Thank you for the {ans['severance_paid']} weeks of severance offered. Unfortunately, I can’t accept it. I believe I am legally entitled to a bigger severance payment, owing to the abruptness of the layoff and the potential damage to my reputation, and career prospects. Under the circumstances, and in the interest of putting this behind us, I would be willing to accept"""
    if ans['severance_demand'] != 'none' and ans['vacation'] != 'none' and ans['apology'] == 'yes':
        # B, C and D
        letter += f""" {ans['severance_demand']} weeks of pay plus all unpaid vacation time that has accrued up until my termination which is {ans['vacation']} weeks. I also want a written apology for all of the hardship that I suffered. """
    elif ans['severance_demand'] != 'none' and ans['vacation'] != 'none':
        # B and C
        letter += f""" {ans['severance_demand']} weeks of pay plus all unpaid vacation time that has accrued up until my termination which is {ans['vacation']} weeks."""
    elif ans['severance_demand'] != 'none':
        # B
        letter += f""" {ans['severance_demand']} weeks of pay. This offer is fair and reasonable to both of us."""
    elif ans['apology'] == 'yes':
        letter += f"""a written apology for all of the hardship that I suffered."""

    letter += f"""<p class="blurText">Despite the shortcomings, I've really enjoyed the last"""
    if ans['months_worked'] != 0 and ans['years_worked'] != 0:
        if ans['years_worked'] != 1:
            letter += f""" {ans['years_worked']} years """
        else:
            letter += ' 1 year '
        if ans['months_worked'] != 1:
            letter += f"""and {ans['months_worked']} months """
        else:
            letter += 'and 1 month '
    else:
        if ans['months_worked'] != 0:
            if ans['months_worked'] != 1:
                letter += f""" {ans['months_worked']} months """
            else:
                letter += ' 1 month '
        else:
            if ans['years_worked'] != 1:
                letter += f""" {ans['years_worked']} years """
            else:
                letter += ' 1 year '
    letter += f"""and getting to know the {ans['company_name']} family. I was truly excited to build something great  - and I have gotten the sense that {ans['company_name']} cares about its employees. Please don't make me feel misled.</p>

    Please let me know your intentions by {ans['response_date']}.
<br><br>
    Thank you,
<br><br>
{ans['name']}"""
    return letter
