"""You have a browser of one tab where you start on the homepage 
and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. 
If you can only return x steps in the history and steps > x, 
you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history.
 If you can only forward x steps in the history and steps > x, 
 you will forward only x steps. Return the current url after forwarding in history at most steps."""



class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.visted_url=[homepage]
        self.curr_URL, self.last_URL = 0, 0
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.curr_URL+=1
        if len(self.visted_url)>self.curr_URL:
            self.visted_url[self.curr_URL]=url
        else :
            self.visted_url.append(url)
            self.last_URL=self.curr_URL

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if steps>len(self.visted_url) :
            self.curr_URL=0
        else :
             self.curr_URL=len(self.visted_url)-steps-1
             print('backurl',self.curr_URL)
        return (self.visted_url[self.curr_URL]) 

        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if steps+self.curr_URL>len(self.visted_url)-1 :
            self.curr_URL=len(self.visted_url)-1
        else :
             self.curr_URL=self.curr_URL+steps
        return (self.visted_url[self.curr_URL]) 

        


# Your BrowserHistory object will be instantiated and called as such:

homepage="leetcode.com"
print(homepage)

obj = BrowserHistory(homepage)
print('initialization,',obj.curr_URL)
obj.visit(url="google.com")
obj.visit(url="google1.com")
print(obj.visted_url)
print('added two url',obj.curr_URL)
param_2 = obj.back(1)
print('back by steps 1,',obj.curr_URL,obj.visted_url[obj.curr_URL])
print(obj.curr_URL)
param_3 = obj.forward(2)
print(param_3)