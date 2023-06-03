import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators,FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../token-service.service';
import { Token } from '@angular/compiler';
import { map } from 'rxjs';
import { Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-updateprofile',
  templateUrl: './updateprofile.component.html',
  styleUrls: ['./updateprofile.component.css']
})
export class UpdateprofileComponent implements OnInit{
  name: string;
  address: string;
  email: string;
  phone:string;
  udata:any;

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
      
  }

  Submit() {
    let body={name:this.name,address:this.address,phone:this.phone,email:this.email};
    console.log(body);
    if(!this.isPhoneValid()){
      alert('Invalid Phone Number');
      return;
    }
    
    this.http.put("http://127.0.0.1:8000/apis/users/profile/update/",body).subscribe((response)=>{
    this.udata=response;
    this.router.navigate(['/dashboard']);
    
    },error=>{});
}
isPhoneValid(){
  return   this.phone.length==10  && !isNaN(Number(this.phone)) ;

}

}
