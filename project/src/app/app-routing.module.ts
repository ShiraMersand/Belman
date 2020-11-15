import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { VolunteerListComponent } from './volunteer/volunteer-list/volunteer-list.component';
import { SchedulingComponent } from './scheduling/scheduling/scheduling.component';
import { VolunteerDetailsComponent } from './volunteer/volunteer-details/volunteer-details.component';


const routes: Routes = [

  { path: "volunteer-list",component: VolunteerListComponent },
  { path: "SchedulingComponent",component: SchedulingComponent },
  { path: "volunteerDetailes/:volunteerId", component: VolunteerDetailsComponent },

];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
