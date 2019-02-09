// https://leetcode.com/problems/unique-email-addresses/submissions/

/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    
    const uniqueEmails = [];
    
    emails.forEach(email => {
        const splitted = email.split("@");
        const local = splitted[0];
        const domain = splitted[1];
        
        let cleanedLocal = [];
        let skip = false;
        for (let alphabet of local) {
            if((alphabet !== '.' && alphabet !== '+') && !skip) cleanedLocal.push(alphabet);
            if(alphabet === '+') skip = true;
        }
        
        const merged = cleanedLocal.join('') + '@' + domain;
        
        if (!uniqueEmails.includes(merged)) uniqueEmails.push(merged);
    });

    return uniqueEmails.length;
};
