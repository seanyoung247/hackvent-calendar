
import { useRef, useState } from 'react';
import CodeSandbox from './components/codesandbox/codesandbox';
import './App.css';


function App() {
  const codePane = useRef(null);
  const [val, setVal] = useState('none');
  const regChange = e => setVal(codePane.current.value);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Hackvent Calendar</h1>
      </header>

      <main className='main'>
        <textarea className='codePane' ref={codePane}
          defaultValue={`function test() {\n  return 5+5;\n}`}/>
        <button onClick={regChange}>Submit</button>

        <CodeSandbox 
          code={val} 
          title="codeSandbox"
          srcDoc="<script src='static/sandbox/sandbox.js'></script>"
        />
      </main>
    </div>
  );
}

export default App;
