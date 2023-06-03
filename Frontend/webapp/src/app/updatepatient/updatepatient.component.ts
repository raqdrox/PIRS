import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators,FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../token-service.service';

@Component({
  selector: 'app-updatepatient',
  templateUrl: './updatepatient.component.html',
  styleUrls: ['./updatepatient.component.css']
})
export class UpdatepatientComponent implements OnInit {
  oid:number;
  
  name:string;
  dob:string;
  gender:string;
  phone:string;
  email:string;
  address:string;
  
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
    id:this.oid,
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
    
};
    console.log(body);
    
    this.http.put("http://127.0.0.1:8000/apis/patient/update/"+this.oid+"/",body).subscribe((response)=>{
    this.add=response;
    if(this.add == "Updated"){
      alert('Patient Record Updated');
  
      
      }
      else{
        alert('Failed to update patient record');
      }
    
    
    },error=>{});
}




  }
