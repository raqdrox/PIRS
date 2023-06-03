import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Data, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../token-service.service';
import { Token } from '@angular/compiler';
import { map } from 'rxjs';
import {NgIf, NgFor} from '@angular/common';
import {MatTableModule} from '@angular/material/table';



@Component({
  selector: 'app-viewpatient',
  templateUrl: './viewpatient.component.html',
  styleUrls: ['./viewpatient.component.css'],
  
  
})
export class ViewpatientComponent implements OnInit {

  ndata:any;
  name:string;
  pdata:any;
  id:Number;
  data:string[];
  dataSource:any;
  clickedRows:any
  

  

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router,
    private authService: AuthService
  ) {}


  ngOnInit(): void{  
   
}

displayedColumns: string[] = ['id', 'name', 'age', 'dob','add','email','contact'];

    
    
submit2(){ 
      console.log(this.id);
      this.http.get("http://127.0.0.1:8000/apis/patient/getbyname/"+this.name+"/").subscribe((response)=>{
      
      this.pdata=response;
      this.data=this.pdata;
      console.log(this.pdata);
      
      this.dataSource = this.data;
      this.clickedRows = new Set<Data>();
      
    
    });
    
    
    }
  }







