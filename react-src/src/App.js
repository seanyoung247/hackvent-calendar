
import CodeSandbox from './components/sandbox/sandbox';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Hackvent Calendar</h1>
      </header>
      <input type="text"></input>
      <CodeSandbox title="codeSandbox" code="Hello World" src="sandbox/sandbox.html"/>
    </div>
  );
}

export default App;
