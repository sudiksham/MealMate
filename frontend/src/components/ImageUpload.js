import React, {useState} from 'react'
import axios from 'axios'
import './ImageUpload.css'

function ImageUpload({addEntry}){
    const [image, setImage] = useState('')
    function handleImage(e){
        console.log(e.target.files[0])
        setImage(e.target.files[0])

        const formData = new FormData()
        formData.append('123', 123)
        formData.append('image', e.target.files[0])
        console.log(formData.get('image'))
        axios({
            method: 'POST',
            url: 'http://127.0.0.1:5000/SUBMITDATA/',
            data: formData,
          }).then((response) => {
            // Assuming response.data contains the new entry
            addEntry(response.data);
          });
        


    }


    function handleAPI(){
        const formData = new FormData()
        formData.append('image', image)
        console.log(formData.get('image'))
        //axios.post("http://127.0.0.1:5000/SUBMITDATA/", formData)
        /*axios({
            method: "POST",
            url: "http://127.0.0.1:5000/SUBMITDATA/",
            data: formData
        })*/
    }
    /* Use some type of checkboxes to tell the program their diet suggestions */
    return (
        <>
        <div className='upload'>
            <input type='file' onChange={handleImage}/>
            <br></br>
            Preferences
            <ul>
                <li>No meat</li>
                <li>No pork</li>
                <li>No fish</li>

            </ul>
        </div>
        
        </>
    )
}

export default ImageUpload;