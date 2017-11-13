## Tornado + AngularJs ToDo App
Structure based on components, easy static files imports, watch and automatic reload static files, logging support...

### Configure
You need to configure `config.py` file before run, or set the next environ variables:
```bash
export APP_SETTINGS="dev"
export PORT=<port_that_you_want>
export COOKIE_SECRET="<your_cookie_secret>"
```

### Run
```bash
git clone https://github.com/mondeja/tornado-angularjs-todo-app.git
cd tornado-angularjs-todo-app
pip3 install -r requirements.txt
cd src
python3 main.py
```

### Tornado + AngularJS tricks
For templates, to avoid double quote braces `{{ }}` template syntax with Angular, you can change with the next config on your modules:
```javascript
app = angular.module('app', []);

app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('//').endSymbol('//');
});
```

