// Sample team data structure for future enhancement
// This shows how you could structure team information for future dynamic pages

const teamMembers = {
  engineers: [
    {
      id: "john-doe",
      name: "John Doe",
      role: "Senior Cloud Architect",
      bio: "AWS cloud architecture expert with 10+ years designing scalable systems",
      fullBio: "AWS cloud architecture expert with 10+ years of experience designing and implementing scalable, enterprise-grade cloud solutions.",
      image: "/assets/images/team/john-doe.jpg",
      specialties: [
        "Cloud Architecture",
        "AWS (10+ years)",
        "System Design",
        "Microservices",
        "Kubernetes",
        "Terraform"
      ],
      certifications: [
        "AWS Certified Solutions Architect – Professional",
        "AWS Certified Solutions Architect – Associate",
        "AWS Certified DevOps Engineer – Professional"
      ],
      experience: "10+ years",
      education: "BS in Computer Science",
      highlights: [
        {
          title: "Enterprise Cloud Migrations",
          description: "Led successful cloud migration initiatives for multiple Fortune 500 companies"
        },
        {
          title: "Scalable Architecture Design",
          description: "Designed and implemented cloud architectures handling millions of requests per second"
        },
        {
          title: "Cost Optimization",
          description: "Achieved average cost reductions of 35% while maintaining performance"
        }
      ],
      engagementModels: ["Project-Based", "Team Augmentation", "Consulting"],
      profileUrl: "/team/engineers/john-doe/"
    }
  ],
  
  leadership: [
    {
      id: "jane-smith",
      name: "Jane Smith",
      role: "Chief Technology Officer",
      bio: "Visionary technology leader with 15+ years building engineering organizations",
      fullBio: "Visionary technology leader with 15+ years of experience building high-performing engineering organizations and driving strategic innovation.",
      image: "/assets/images/team/jane-smith.jpg",
      position: "Chief Technology Officer",
      specialties: [
        "Technology Strategy",
        "Organization Building",
        "Engineering Leadership",
        "Cloud Architecture",
        "Team Development"
      ],
      achievements: [
        "Built engineering teams from 5 to 100+ engineers",
        "Named to '40 Under 40' Technology Leaders",
        "Regular conference speaker",
        "Published on microservices and distributed systems"
      ],
      education: "MBA in Business Administration, BS in Computer Science",
      experience: "15+ years",
      profileUrl: "/team/leadership/jane-smith/"
    }
  ],

  services: [
    {
      id: "engineering-consulting",
      name: "Engineering Consulting",
      shortDesc: "Strategic guidance on system design, architecture, and technical strategy",
      fullDesc: "Strategic guidance on system design, architecture patterns, technology selection, and technical roadmap planning. We help you make informed decisions that align with your business goals.",
      icon: "📋",
      link: "/services/"
    },
    {
      id: "software-development",
      name: "Software Development",
      shortDesc: "Custom software solutions built with modern technologies",
      fullDesc: "Custom software solutions built with modern technologies, clean architecture, and best practices. From greenfield projects to enhancements, we deliver quality code and reliable systems.",
      icon: "💻",
      link: "/services/"
    },
    {
      id: "cloud-architecture",
      name: "Cloud Architecture & Migration",
      shortDesc: "Design and implement scalable cloud solutions",
      fullDesc: "Design and implement scalable cloud solutions. Whether you're moving to the cloud for the first time or optimizing existing deployments, we provide comprehensive support across AWS, Azure, and GCP.",
      icon: "☁️",
      link: "/services/"
    },
    {
      id: "resource-placement",
      name: "Resource Placement",
      shortDesc: "Access vetted engineering talent for your projects",
      fullDesc: "Access vetted engineering talent for your projects. Whether you need specialized skills for a specific project or long-term team augmentation, we connect you with experienced professionals.",
      icon: "👥",
      link: "/services/resource-placement/"
    },
    {
      id: "research-development",
      name: "Research & Development",
      shortDesc: "Create proprietary technologies and innovative solutions",
      fullDesc: "Cutting-edge research and development to create proprietary technologies, software, and systems that address emerging engineering challenges.",
      icon: "🚀",
      link: "/services/rd/"
    }
  ]
};

// Example usage for future dynamic pages:
// 
// Display all engineers:
// teamMembers.engineers.map(eng => `<div>${eng.name} - ${eng.role}</div>`)
//
// Find specific engineer:
// teamMembers.engineers.find(eng => eng.id === 'john-doe')
//
// Get all specialties:
// teamMembers.engineers.flatMap(eng => eng.specialties)
//
// Display services:
// teamMembers.services.map(svc => `<div>${svc.icon} ${svc.name}</div>`)

export default teamMembers;
