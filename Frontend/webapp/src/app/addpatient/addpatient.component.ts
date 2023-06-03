import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators,FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../token-service.service';
import { Token } from '@angular/compiler';
import { map } from 'rxjs';
import { Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-addpatient',
  templateUrl: './addpatient.component.html',
  styleUrls: ['./addpatient.component.css']
})
export class AddpatientComponent implements OnInit {
  id:number;
  name:string;
  dob:string;
  gender:string;
  phone:string;
  email:string;
  address:string;
  last_updated_by:string;
  blood_group:string;
  diseases:string;
  allergies:string;
  height:number;
  weight:number;
  name2:string;
  phone2:string;
  finger_id:number;
  add:any;

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
      
  }
  
  Submit() {
    let body={
    name: this.name,
    dob: this.dob,
    gender:this.gender,
    phone: this.phone,
    email: this.email,
    address:this.address,
    medical_data: {
        blood_group: this.blood_group,
        diseases:this.diseases,
        allergies: this.allergies,
        height: this.height,
        weight: this.weight
    },
    emergency_contact: {
        name: this.name2,
        phone: this.phone2
    },
    finger_id:this.finger_id
};
    console.log(body);

    if(!this.isPhoneValid()){
      alert('Invalid Phone Number');
      return;
    }
    
    this.http.post("http://127.0.0.1:8000/apis/patient/create/",body,{ observe: 'response' }).subscribe(response=>{
   
    console.log(response);
    alert('Patient Added');
    window.location.reload();

    },error=>{       alert('Failed to add patient');
    window.location.reload();
  });
  //window.location.reload();

}

isPhoneValid(){
  return   this.phone.length==10 && this.phone2.length==10 && !isNaN(Number(this.phone)) && !isNaN(Number(this.phone2));

}
  }


