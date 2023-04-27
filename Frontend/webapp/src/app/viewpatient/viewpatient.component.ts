import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../token-service.service';
import { Token } from '@angular/compiler';
import { map } from 'rxjs';



@Component({
  selector: 'app-viewpatient',
  templateUrl: './viewpatient.component.html',
  styleUrls: ['./viewpatient.component.css']
})
export class ViewpatientComponent implements OnInit {

  ndata:any;
  name:string;
  pdata:any;
  id:Number
  
  

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router,
    private authService: AuthService
  ) {}


  ngOnInit(): void{  
   
}


    
    
submit2(){ 
      console.log(this.id);
      this.http.get("http://127.0.0.1:8000/apis/patient/get/"+this.id+"/").subscribe((response)=>{
      
      this.pdata=response;
      console.log(this.pdata);
    
    });
      
    }
  }







