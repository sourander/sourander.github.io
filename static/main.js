const apiUrl = 'https://api.github.com/users/sourander/repos';
const container = document.getElementById('projects-container');

fetch(apiUrl)
    .then(response => response.json())
    .then(repos => {
        console.log('Fetching siteinfo.json for each repository...');
        repos.forEach(repo => {
            const siteinfoUrl = `https://raw.githubusercontent.com/sourander/${repo.name}/master/README.md`;

            fetch(siteinfoUrl)
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error('siteinfo.json not found');
                    }
                })
                .then(siteinfo => {
                    const projectElement = document.createElement('div');
                    projectElement.innerHTML = `
                        <h2>${repo.name}</h2>
                        <p>Description: ${siteinfo.description}</p>
                        <p>Package Versions: ${siteinfo.package_versions.join(', ')}</p>
                        <!-- Add more information as needed -->
                    `;
                    container.appendChild(projectElement);
                })
                .catch(error => {
                    console.error(`Error fetching siteinfo.json for ${repo.name}: ${error.message}`);
                });
        });
    })
    .catch(error => {
        console.error(`Error fetching GitHub repositories: ${error.message}`);
    });
  