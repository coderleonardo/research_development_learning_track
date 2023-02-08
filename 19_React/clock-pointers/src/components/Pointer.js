import { useEffect, useRef } from "react";

const Pointer = ( {rotateVal }) => {

    const pointerHandle = useRef(null);

    function getRotateVal(rotateVal) {
        return rotateVal + 1;
    }
  
    useEffect(() => {
        setInterval(() => { 
            
            let rotateValues = getRotateVal()
            // let date = new Date();
            // let rotateValues = date.getSeconds();


          pointerHandle.current.style.transform = `rotateZ(${rotateValues * 6}deg)`;
          console.log(rotateValues)
          console.log(pointerHandle.current.style.transform)
        }, 1000);
    }, []);
  
    return (
        <div className="pointer-container">
        <div className="pointer">
          <div ref={pointerHandle} className="ptr" id="ptr">
            <div className="pt"></div>
          </div>
        </div>
      </div>
    );
  }

export default Pointer;